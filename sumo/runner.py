#!/usr/bin/env python
# coding: utf-8
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2020 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    runner.py
# @author  Lena Kalleske
# @author  Daniel Krajzewicz
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @date    2009-03-26

from __future__ import absolute_import
from __future__ import print_function

import csv
import os
import sys
import optparse
import random

# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa

# ----- GLOVAL VARS -----

# ----- functions -----

def generate_routefile():
    random.seed(42)  # make tests reproducible
    N = 3600  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 11
    pNS = 1. / 30
    with open("data/cross.rou.xml", "w") as routes:
        print("""<routes>
        <vType id="typeWE" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" \
guiShape="passenger"/>
        <vType id="typeNS" accel="0.8" decel="4.5" sigma="0.5" length="7" minGap="3" maxSpeed="25" guiShape="bus"/>

        <route id="right" edges="51o 1i 2o 52i" />
        <route id="left" edges="52o 2i 1o 51i" />
        <route id="down" edges="54o 4i 3o 53i" />""", file=routes)
        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="right_%i" type="typeWE" route="right" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="left_%i" type="typeWE" route="left" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="down_%i" type="typeNS" route="down" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
        print("</routes>", file=routes)

# The program looks like this
#    <tlLogic id="0" type="static" programID="0" offset="0">
# the locations of the tls are      NESW
#        <phase duration="31" state="GrGr"/>
#        <phase duration="6"  state="yryr"/>
#        <phase duration="31" state="rGrG"/>
#        <phase duration="6"  state="ryry"/>
#    </tlLogic>

class AddVehicleHandler:
    #  ----- 道路の構成 -----
    # edge id: "1to2", lane id "1to2_0" --------------- | ----- edge id: "out"
    # edge id: "1to2", lane id "1to2_1" --------------- | ----- edge id: "gneE7"
    # edge id: "1to2", lane id "1to2_2" --------------- | ----- edge id: "gneE8"
    # edge id: "1to2", lane id "1to2_3" --------------- | ----- edge id: "gneE9"

    # ----- メモ -----
    # 車両は　edge id: "1to2" のいずれかのレーン上に生成され，　
    # edge id: "out" ~ "gneE9" のいずれかの道路が目的地として設定されている．

    ADD_VEHICLE_NUM_AT_SAME_TIME = 100
    ADD_VEHICLE_INTERVAL = 2000.0 * 1000   # (msec)
    START_EDGES = ["1to2"]
    GOAL_EDGES = ["gneE9", "gneE8", "gneE7", "out"]

    def __init__(self, simulation_start_time):
        self.next_vehicle_add_time = simulation_start_time + AddVehicleHandler.ADD_VEHICLE_INTERVAL
        self.next_vehicle_index = 0
        self.next_route_index = 0

        # ----- register routes -----
        self.route_ids = []
        for start_edge in AddVehicleHandler.START_EDGES:
            for goal_edge in AddVehicleHandler.GOAL_EDGES:
                self.route_ids.append(self.register_new_route(start_edge, goal_edge))

    def add_vehicle_handle(self, current_time):
        if self.is_update_next_vehicle_add_time(current_time):
            self.update_next_vehicle_add_time(current_time)
            self.add_vehicles(AddVehicleHandler.ADD_VEHICLE_NUM_AT_SAME_TIME)

    def add_vehicle_at_random_route(self):
        self.register_new_vehicle(random.choice(self.route_ids))

    def add_vehicles(self, given_num=1):
        for i in range(0, given_num):
            self.add_vehicle_at_random_route()

    def is_update_next_vehicle_add_time(self, current_time):
        return self.next_vehicle_add_time <= current_time

    def register_new_route(self, start_edge, goal_edge):
        new_route_id = "rou_" + str(self.next_route_index)

        traci.route.add(new_route_id, [start_edge, goal_edge])
        self.next_route_index = self.next_route_index + 1

        return new_route_id

    def register_new_vehicle(self, route_id):
        new_vehicle_id = "veh_" + str(self.next_vehicle_index)

        traci.vehicle.add(new_vehicle_id, route_id, departLane="random")
        self.next_vehicle_index = self.next_vehicle_index + 1

        print(f"veh_id: {new_vehicle_id:10}, destination edge: {traci.route.getEdges(route_id)[-1]:10}")
        return self.next_vehicle_index

    def update_next_vehicle_add_time(self, current_time):
        self.next_vehicle_add_time = current_time + AddVehicleHandler.ADD_VEHICLE_INTERVAL

class ArrivedVehicleHandler:
    def __init__(self):
        self.arrived_vehicles = []

    def update_arrived_vehicles(self):
        self.arrived_vehicles.extend(traci.simulation.getArrivedIDList())
        self.arrived_vehicles = list(set(self.arrived_vehicles))

class EvaluationHandler:
    ALL_RESULT_PATH = "./result/all/"
    SUMMARY_RESULT_PATH = "./result/summary/"

    def __init__(self, veh_num, apply_prop, method_name):
        self.data = []
        self.veh_num = veh_num
        self.apply_prop = apply_prop
        self.method_name = method_name

    def snapshot(self):
        for veh_id in traci.vehicle.getIDList():
            self.data.append(self.formatted_data(veh_id))

    def formatted_data(self, veh_id):
        formatted_data = {
            "id": veh_id,
            "time": traci.simulation.getTime(),
            "speed": traci.vehicle.getSpeed(veh_id),
        }

        return formatted_data

    def save_as_csv(self, file_path, dict_data):
        try:
            with open(file_path, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=dict_data[0].keys())
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)

        except IOError:
            print("I/O error")

    def save_all(self):
        self.save_as_csv(EvaluationHandler.ALL_RESULT_PATH + self.save_file_name(), self.data)

    def save_summary(self):
        self.save_as_csv(EvaluationHandler.SUMMARY_RESULT_PATH + self.save_file_name(), self.summary_data())

    def save_file_name(self):
        return f"{self.method_name}_num_{self.veh_num}_apply_prop_{self.apply_prop}.csv"

    def summary_data(self):
        all_vehicle_speed_list = [d["speed"] for d in self.data]

        summary_data = [{
            "average_speed": sum(all_vehicle_speed_list) / len(all_vehicle_speed_list)
        }]

        return summary_data

class FinishHandler:
    ARRIVED_VEHICLE_THRETHOLD = 100

    def __init__(self):
        pass

    def is_finish(self, arrived_vehicles=[]):

        if traci.simulation.getMinExpectedNumber() <= 0:
            return True
        elif FinishHandler.ARRIVED_VEHICLE_THRETHOLD <= len(list(set(arrived_vehicles))):
            return True

        return False

def vehicle_manipulation():
    # この下に好きにコードを書いてください.

    # この上に好きにコードを書いてください.
    pass

def run(apply_prop, add_vehicle_handler, arrived_vehicle_handler, finish_handler, evaluation_handler):
    """execute the TraCI control loop"""
    add_vehicle_handler.add_vehicles(AddVehicleHandler.ADD_VEHICLE_NUM_AT_SAME_TIME)

    while finish_handler.is_finish(arrived_vehicle_handler.arrived_vehicles) is False:
        arrived_vehicle_handler.update_arrived_vehicles()
        add_vehicle_handler.add_vehicle_handle(traci.simulation.getTime())
        evaluation_handler.snapshot()

        if apply_prop is True:
            vehicle_manipulation()
        else:
            pass

        traci.simulationStep()

    evaluation_handler.save_all()
    evaluation_handler.save_summary()
    traci.close()
    sys.stdout.flush()

def sample(apply_prop, sample_num, add_vehicle_handler, arrived_vehicle_handler, finish_handler, evaluation_handler):
    add_vehicle_handler.add_vehicles(sample_num)

    while 0 < traci.simulation.getMinExpectedNumber():
        evaluation_handler.snapshot()

        if apply_prop is True:
            vehicle_manipulation()
        else:
            pass

        traci.simulationStep()

    evaluation_handler.save_all()
    evaluation_handler.save_summary()
    traci.close()
    sys.stdout.flush()


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    optParser.add_option("--sample", action="store_true",
                         default=False, help="run with only one vehicle")
    optParser.add_option("--sample_num", action="store", type="int",
                         default=1, help="the number of vehicles in a sample scenario")
    optParser.add_option("--unapply_prop", action="store_true",
                         default=False, help="flag to decide applying the proposed method.")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation
    generate_routefile()

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary,
        "-c"                    , "my_data/hello.sumocfg",
        "--tripinfo-output"     , "tripinfo.xml",
        "--step-length"         , "0.1",
        "--random"
    ])

    add_vehicle_handler = AddVehicleHandler(traci.simulation.getTime())
    arrived_vehicle_handler = ArrivedVehicleHandler()
    finish_handler = FinishHandler()
    apply_prop = (not options.unapply_prop)

    if options.sample:
        evaluation_handler = EvaluationHandler(options.sample_num, apply_prop, "sample")
        print(f">> This code saves its results into {EvaluationHandler.ALL_RESULT_PATH + evaluation_handler.save_file_name()}")
        sample(apply_prop, options.sample_num, add_vehicle_handler, arrived_vehicle_handler, finish_handler, evaluation_handler)
    else:
        evaluation_handler = EvaluationHandler(AddVehicleHandler.ADD_VEHICLE_NUM_AT_SAME_TIME, apply_prop, "run")
        print(f">> This code saves its results into {EvaluationHandler.ALL_RESULT_PATH + evaluation_handler.save_file_name()}")
        run(apply_prop, add_vehicle_handler, arrived_vehicle_handler, finish_handler, evaluation_handler)

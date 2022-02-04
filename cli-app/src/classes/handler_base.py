import os
import csv
import pickle


class HandlerBase:
    def __init__(self, file_path, csv_file_path):
        self.pickle_file_path = file_path
        self.csv_file_path = csv_file_path

    @property
    def data(self):
        return self.__load_data(self.pickle_file_path)


    def __load_data(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                return pickle.load(f)

        else:
            return []


    def add_data(self, new_data):
        self.update_data(self.data + [new_data])

    def delete_by_id(self, id):
        self.update_data([d for d in self.data if int(d.id) != int(id) ])

    def all(self):
        return self.data

    def update_data(self, data_list):
        with open(self.pickle_file_path, 'wb') as f:
            pickle.dump(data_list, f)


    def csv_dump(self):
        data = [d.__dict__ for d in self.data]

        if len(data) <= 0:
            return

        with open(self.csv_file_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


    def csv_patch(self):
        raise Exception("Uninheritanced ...")

    def find_by_id(self, id):
        for d in self.all():
            if d.id == int(id):
                return d

            else:
                continue

        return None

    def show(self):
        for d in self.data:
            print(d.__dict__)

    def unique_id(self):
        return max([int(d.id) for d in self.data] + [-1]) + 1

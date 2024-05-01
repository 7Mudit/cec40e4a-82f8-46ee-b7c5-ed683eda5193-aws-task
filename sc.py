import os
import random

# Configuration
data_root = "path"  
output_directory = "output"
train_file = os.path.join(output_directory , "train_lst.lst")
validation_file = os.path.join(output_directory , "validation_lst.lst")
num_images_per_class = 10
train_split = 8 / num_images_per_class  # Assuming an approximate 80/20 split

# Class folders
class_folders = [
    "argent_piece_monnaie",
    "boite_oeuf",
    "briquet_plastique",
    "elec_ordinateur_souris",
    "food_tomates",
    "vetements_montre",
]

# simulating initial setup
# os.makedirs(data_root , exist_ok=True)
# for folder in class_folders :
#     full_path = os.path.join(data_root , folder)
#     os.makedirs(full_path , exist_ok=True)

#     # create sample image files
#     for i in range(10):
#         with open(os.path.join(full_path , f"image{i:04d}.jpg") , 'w') as f:
#             f.write("This is a sample image file.\n")


def process_class_folder(folder_name, train_list, validation_list):
    """Processes a single class folder"""
    folder_path = os.path.join(data_root , folder_name)
    class_id = class_folders.index(folder_name)
    all_image_paths = os.listdir(folder_path)
    random.shuffle(all_image_paths)  # Shuffle images within the class

    for image_index, image_path in enumerate(all_image_paths):
        relative_image_path = os.path.join(folder_path, image_path)
        if image_index < train_split * num_images_per_class:
            train_list.append(f"{image_index}\t{class_id}\t{relative_image_path}\n")
        else:
            validation_list.append(f"{image_index}\t{class_id}\t{relative_image_path}\n")


# Main logic
train_list = []
validation_list = []

for class_folder in class_folders:
    process_class_folder(class_folder, train_list, validation_list)

random.shuffle(train_list)  # Shuffle the entire training list
random.shuffle(validation_list)  # Shuffle the entire validation list

with open(train_file, "w") as f:
    f.writelines(train_list)

with open(validation_file, "w") as f:
    f.writelines(validation_list)

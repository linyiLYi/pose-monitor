import os

data_dir = "pose_data"
for pose_dir in os.listdir(data_dir):
    full_pose_dir = os.path.join(data_dir, pose_dir)
    for i, img_filename in enumerate(os.listdir(full_pose_dir)):
        old_img_path = os.path.join(full_pose_dir, img_filename)
        new_img_path = os.path.join(full_pose_dir, "{}_{:03d}.jpg".format(pose_dir, i + 1))
        os.rename(old_img_path, new_img_path)

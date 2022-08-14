
import os 

#模型地址
trojan_casual_dir = "/home/rui/Desktop/disk2/data/trojan_casual"
model_dir = os.path.join(trojan_casual_dir,"models")


#dataloader地址
dataloader_dir = os.path.join(trojan_casual_dir,"dataloader")


#square trigger
trigger_img_path = os.path.join(trojan_casual_dir,"image_trigger/trigger_06.jpg")



learning_rate = 0.005
batch_size = 128
test_batch_size = 128
trigger_size = 8
trigger_pos = 0
inject_r = 0.1
untrust_prop = 0.95
ret = 175# ret是控制mask透明度的阈值（175）
target_label = 9

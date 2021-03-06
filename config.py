import math

seed = 0

THRESHOLD_POSITIVE = 0.1
THRESHOLD_NEGATIVE = 0

threshold_point = 25
window = 120

sigma = 18.5
sigma_aff = 20

boundary_character = math.exp(-1/2*(threshold_point**2)/(sigma**2))
boundary_affinity = math.exp(-1/2*(threshold_point**2)/(sigma_aff**2))

threshold_character = boundary_character + 0.03
threshold_affinity = boundary_affinity + 0.03

threshold_character_upper = boundary_character + 0.2
threshold_affinity_upper = boundary_affinity + 0.2

scale_character = math.sqrt(math.log(boundary_character)/math.log(threshold_character_upper))
scale_affinity = math.sqrt(math.log(boundary_affinity)/math.log(threshold_affinity_upper))

dataset_name = 'ICDAR2013_ICDAR2017'
test_dataset_name = 'ICDAR2013'

print(
	'Boundary character value = ', boundary_character,
	'| Threshold character value = ', threshold_character,
	'| Threshold character upper value = ', threshold_character_upper
)
print(
	'Boundary affinity value = ', boundary_affinity,
	'| Threshold affinity value = ', threshold_affinity,
	'| Threshold affinity upper value = ', threshold_affinity_upper
)
print('Scale character value = ', scale_character, '| Scale affinity value = ', scale_affinity)
print('Training Dataset = ', dataset_name, '| Testing Dataset = ', test_dataset_name)

DataLoaderSYNTH_base_path = '/content/CRAFT_Train/SynthText/Images'
DataLoaderSYNTH_mat = '/content/CRAFT_Train/SynthText/gt.mat'
DataLoaderSYNTH_Train_Synthesis = '/content/CRAFT_Train/Models/SYNTH/train_synthesis/'

DataLoader_Other_Synthesis = '/content/CRAFT_Train/Save/'
Other_Dataset_Path = '/content/CRAFT_Train/'
save_path = '/content/CRAFT_Train/Models/WeakSupervision/'
images_path = '/content/CRAFT_Train/Images'
target_path = '/content/CRAFT_Train/Generated'

Test_Dataset_Path = '/content/CRAFT_Train/'

threshold_word = 0.7
threshold_fscore = 0.5

dataset_pre_process = {
	'ic13': {
		'train': {
			'target_json_path': None,
			'target_folder_path': None,
		},
		'test': {
			'target_json_path': None,
			'target_folder_path': None,
		}
	},
	'ic15': {
		'train': {
			'target_json_path': "/content/CRAFT_Train/icdar2015/train/gt",
			'target_folder_path': "/content/CRAFT_Train/icdar2015/train/img",
		},
		'test': {
			'target_json_path': "/content/CRAFT_Train/icdar2015/val/gt",
			'target_folder_path': "/content/CRAFT_Train/icdar2015/val/img",
		}
	}
}

start_iteration = 0
skip_iterations = []

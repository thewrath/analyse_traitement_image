with import <nixpkgs> {};
(python38.withPackages (ps: [
	ps.jupyter 
	ps.tensorflow 
	ps.Keras 
	ps.numpy 
	ps.scikitlearn 
	ps.matplotlib 
	ps.pandas 
	ps.imageio
	ps.scikitimage
	ps.pytorch
	ps.torchvision
])).env

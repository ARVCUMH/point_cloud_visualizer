import open3d
import glob
import os
import numpy as np
from plyfile import PlyData, PlyElement

def vis_dict(dict):
    pcds = sorted(glob.glob('{}/*.ply'.format(dict)))
    vis = open3d.visualization.VisualizerWithKeyCallback()
    vis.create_window()
    idx = 0
    pcd = open3d.io.read_point_cloud(pcds[idx])
    vis.add_geometry(pcd)


    def right_click(vis):
        nonlocal idx
        idx = idx + 1
        vis.clear_geometries()
        pcd = open3d.io.read_point_cloud(pcds[idx])
        print(pcds[idx])
        plydata = PlyData.read(pcds[idx])
        labels = plydata.elements[0].data['labels']
        color = []
        for i in labels:
            if i == 1:
                color.append([95,158,160])
            else:
                color.append([106,90,205])
        pcd.colors = open3d.utility.Vector3dVector(np.asarray(color)/255)
        vis.add_geometry(pcd,reset_bounding_box=False)

    def exit_key(vis):
        vis.destroy_window()

    vis.register_key_callback(262, right_click)
    vis.register_key_callback(32, exit_key)
    vis.poll_events()
    vis.run()
    vis.destroy_window()



if __name__ == '__main__':
    root = "/media/arvc/Extreme SSD/dataset_recortado_normales_vecinos/usl_voxel_neighbour/sequences/1"
    vis_dict(root)
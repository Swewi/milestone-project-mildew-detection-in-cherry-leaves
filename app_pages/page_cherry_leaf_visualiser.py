import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_cherry_leaf_visualiser_body():
    st.write("### Powdery mildew detector")
    st.info(
        f"* The client is interested in conducting a study that visually "
        f"differentiates between infected and non-infected leaves.")

    st.write(
        f"* For more in depth information, you can check out the associated "
        f"[README](https://github.com/Swewi/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md) file.")

    st.success(
        f"* The fungal infection called 'Powdery Mildew' is of concern within the cherry industry "
        f"because it spreads within an orchard very quickly and easily. "
        f"As a consequence of this the client requires a quick way of identifying infected trees to "
        f"minimise infection."
    )
    
    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
      
      avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_healthy.png")
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")

      st.warning(
        f"* We observed that the average and variability in the images does not reveal "
        f"any clear patterns that would allow us to intuitively differentiate between "
        f"infected and non-infected leaves. "
        f"However, the infected leaves do have a greater abundance of white lines "
        f"covering the visable surface.")

      st.image(avg_powdery_mildew, caption='Uninfected Leaf - Average and Variability')
      st.image(avg_healthy, caption='Powdery Mildew Infected - Average and Variability')
      st.write("---")

    if st.checkbox("Differences between average infected and average uninfected leaves"):
          diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

          st.warning(
            f"* We observed that this study did not reveal patterns that would allow us "
            f"to intuitively differentiate between the images.")
          st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on the 'Create Montage' button")
      my_data_dir = 'inputs/cherry-leaves/cherry-leaves'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
        image_montage(dir_path= my_data_dir + '/validation',
                      label_to_display=label_to_display,
                      nrows=8, ncols=3, figsize=(10,25))
      st.write("---")



def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if montage space is greater than subset size
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)
    # plt.show()


  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")
# Detection of powdery mildew on cherry leaves

Powdery mildew is a common fungal infection that affects cherry trees, often causing a web of white fibres covering the leaves. This infection can lead to premature leaf drop, reduced photosynthesis, and weakened trees. Over time, affected cherry trees may exhibit stunted growth, decreased fruit production, and lower fruit quality. In severe cases, the overall health and longevity of the tree can be compromised, making it more susceptible to other diseases and environmental stresses. As such it is crucial to monitor cherry orchards for powdery mildew infection, this is where this project enters.

***

**[Link to live Streamlit app](https://cherryleafinfect-4f02b3a49366.herokuapp.com)**

This is the Milestone Project for Predictive Analytics section of the Full Stack Developer Course taught through Code Institute
***

## Dataset Content

* The dataset for this project is sourced from **[Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)**.
* The dataset contains over 4,000 images of both infected and healthy cherry leaves, all taken with the client's permission from trees within their cherry orchards. Although the company has a varied portfolio, cherries remain one of their most important crops. Consequently, they are seriously concerned about the potential impact of supplying sub-standard products.
* Due to size constraints for deploying to Heroku I have been forced to resize the images.  Originally the images were all *256 x 256*, after some testing I have resized them to *175 x 175*, this size minimises loss of quality while just scrapping under the Heroku size limit.

## Business Requirements

*For clarrity this is an eductaion based assignment, as such the company used here is for illustration purposes.*

Farmy & Foods' cherry orchard is facing a crisis as workers have noticed typical signs of powdery mildew on some trees. Currently, staff manually verify the presence of powdery mildew, spending approximately 30 minutes collecting and visually inspecting leaves. If powdery mildew is detected, fungicide is applied. With thousands of cherry trees spread across multiple locations nationwide, this process is not scalable, limiting its effectiveness.

We have been approached to find a scalable, quick, and easy solution that remains cost-effective. During a brainstorming session, the IT team suggested a machine learning approach. This solution would enable rapid detection and be simple to use in the field, utilising images of tree leaves. Farmy & Foods already monitors other crops using similar manual processes. If this initiative is successful, it could well be implemented for other crops.

The data used for this project is a collection of cherry leaf images provided by Farmy & Foods, taken from their orchards.

## Hypothesis and how to validate?

* That infected cherry leaves will have clear visual signs of infection across the surface of a leaf, that will differentiate them from healthy leaves.

  * Validation - The model successfully detected the differences between infected and healthy leaves, learning to differentiate and generalise to make accurate predictions. A good model trains its ability to predict classes on a batch of data without adhering too closely to that specific set. This way, the model generalises and reliably predicts future observations because it didn't merely 'memorise' the relationships between features and labels seen in the training dataset but learned the general patterns from features to labels.

* An Image Montage shows that typically an infected leaf is covered in a web of white fibers. Average Image, Variability Image and Difference between Averages studies did not reveal any clear pattern to differentiate one from another.

  * Validation - The analysis of the Image Montage confirmed that the visual differences between infected and healthy leaves were subtle and not easily distinguishable using average and variability images alone. Despite this, the model demonstrated a perfect F1 score of 1.0, indicating that it successfully learned to identify the specific features distinguishing infected from healthy leaves, even when these features were not apparent in simple image comparisons. This indicates that the model was not misled by the visual complexity of the infected leaves but instead captured the underlying patterns necessary for accurate classification.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one infected with powdery mildew.
  * Using streamlit to create a dashboard that is easy to navigate and intuitive, utilising an interactive sidebar:
    * Contains a page "Cherry Leaf Visualaiser" that displays different diagonistic images depending on checkbox.
    * An "average" and "variabiltiy" side by side for both healthy and infected leaves, these are similar to the `mean` and `standard deviation` if this was numerical instead of visual.
    * A side by side of the averages of both healthy and infected images with the difference between them.
    * A montage of random images based on the label for quick visual reference.

* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
  * Using streamlit to create a dashboard that is easy to navigate and intuitive, utilising an interactive sidebar:
    * Contains a page "Powdery Mildew Detector" that allows you to upload your own images to be tested.
    * It will reject images that are too big or the wrong format, currently included formats in this app;
      * jpg, jpeg, and png.
    * It will output the image and a report that can be downloaded or screen captured with the information.

![Screenshot of the report field on visualiser page](readme_images/report%20from%20test%20images.png)

## Machine Learning Business Case

* We aim to develop a machine learning model to predict whether a leaf is infected with powdery mildew using an image database provided by the client. This problem falls under supervised learning and involves building a binary (two-class), single-label, classification model.
* Our ideal outcome is to provide the clients a more reliable, faster, and cost effective product for powdery mildew detection.
* The model success metrics are:
  * Accuracy of 97% or above on the test set.
* The model will indicate if a leaf has powdery mildew and provide the probability of infection. Staff can take pictures of leaves and upload them directly to the app, the images will then be analysed and a prediction report created that can be acted upon immediately.

![Screenshot of sample output from powdery mildew visualiser](readme_images/visulaiser_output.jpg)

* The current detection method relies on manual inspection. Currently staff spend around 30 minutes per tree, taking a number of samples and visually checking if they are healthy or infected. The current method is slow and prone to inaccuracies due to human error.
* The training data used for the model came from the leaves database provided by client and uploaded on Kaggle. This dataset contains 4208 images of cherry leaves, split evenly between healthy and infected.

## Dashboard Design - Streamlit app

### Page 1 - Project Summary

* Contains several sections covering a quick overview of the apps purpose:
  * **General Information** very brief overview of the reasoning behond this project.
  * **Project Dataset** description of the dataset as sourced from kaggle.
* A link to the Readme

### Page 2 - Cherry Leaf Mildew Detector

* Contains several sections covering the visualiser page:
  * Two small paragraphs with page information.
  * A link to the Readme
  * Three checkbox options that display different information:
    * Including the following overview images

![Screenshot of the healthy images overview](readme_images/healthy.jpg)

![Screenshot of the infected images overview](readme_images/infected.jpg)

* Differences between the datasets

![Screenshoot of the differences between the datasets](readme_images/differences.jpg)

* An image montage compiler of either healthy or infected leaves depending on the selection.

* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment - Using Github and Heroku

### Cloning the Repository

* On Github navigate to the repository "<https://github.com/Swewi/milestone-project-mildew-detection-in-cherry-leaves/tree/main>"
* Click "Code" drop down menu - a green button shown right above the file list.
* Copy the URL of the repository using "HTTPS", "SSH" or "Github CLI".
* Open Git Bash.
* Change the current working directory to the location where you want the cloned directory.
* Type "git clone", and then paste the URL copied earlier.
* Press enter to create local clone. A clone of the repository will now be created.

* For more details on how to clone the repository in order to create a copy for own use refer to the site:
[Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Forking a Repository

* On Github navigate to the repository "<https://github.com/Swewi/milestone-project-mildew-detection-in-cherry-leaves/tree/main>"
* Click "Fork" located towards top right corner on GitHub page.
* Select "owner" for the forked repository from the dropdown menu under "owner".
* It will create forked repo under the same name as original by default. But you can type a name in "Repository name" or add a description in "Description" box.
* Click on "Create fork". A forked repo is created.

#### Important Information about forking a repository

* Forking allows you to make any changes without affecting original project. You can send the the suggestions by submitting a pull request. Then the Project Owner can review the pull request before accepting the suggestions and merging them.
* When you have fork to a repository, you don't have access to files locally on your device, for getting access you will need to clone the forked repository.
* For more details on how to fork the repo, in order to for example suggest any changes to the project you can:
[Forking a Repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

### Deploying the app - Heroku

* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.

* **Important information for running an older version of python:**

  * If an error occurs when deploying stating that the Python version is not available, it is probably due to the stack used for the application. To fix this, log in to the Heroku command line interface (CLI) and use the following command to set the stack to Heroku-20.

    * heroku stack:set heroku-20 -a your-app-name
      * In this case the your-app-name is **cherryleafinfect**

* The app is deployed from Heroku using the following steps:
  * Create Heroku account.
  * In the top right, click 'New'.
  * Click 'Create new app'.
  * Give your app a name and select your region from drop down.
  * Click 'Create new app'.
  * Select 'Deploy' tab at the top.
  * Select 'Github' from 'Deployment method'.
  * Type the name given to your project in Github and click 'search'.
  * Scroll down and select Manual deployment method.
  * You can also use Auto deployment method to allow the project to update every time you push the code.
  * You can now click to view the app ready and running.
  * If the slug size is too large, then add large files not required for the app to run to the .slugignore file.

#### Important Information about forking a repository - Heorku

* The web application is displayed and deployed using template provided by Code Institute to test the code.
* For this project I used Manual deployment method to deploy the current state of the branch, every time I pushed the code from Gitpod.

* The App live link: `https://cherryleafinfect-4f02b3a49366.herokuapp.com/`

## Main Data Analysis and Machine Learning Libraries

* Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* https://plantwiseplusknowledgebank.org/doi/full/10.1079/pwkb.species.42639
* https://www.canr.msu.edu/ipm/diseases/powdery_mildew_of_cherry?language_id=
* https://www.wildfooduk.com/wild-plants/wild-cherry/
* https://attra.ncat.org/publication/cherry-diseases/
* https://extension.usu.edu/planthealth/ipm/notes_ag/fruit-powdery-mildew

### Media

' The photos used on the home and sign-up page are from This Open-Source site.
' [The images used for testing visualiser were taken from this site.](https://www.wildfooduk.com/wild-plants/wild-cherry/)

## Acknowledgements

* My Grandmother who passed suddenly not long before I started this portion of the course
  * Edna Bellamy 1927 - 2024, Matamata, New Zealand
* My partner for dealing with freak outs and frustration

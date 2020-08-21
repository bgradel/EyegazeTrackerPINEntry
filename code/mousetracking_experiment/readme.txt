Eye Gaze Study Readme

The experiment:
The experiment is built in lab.js. Lab.js has a builder located here: https://labjs.felixhenninger.com/#
In the builder you can run and edit the lab. It will save the lab to a json file
The current experiment is saved as mousetracker.lab.json\
The results of an experiment are saved to a csv file

The builder runs on html, css and javascript
You can find documentation here: https://labjs.readthedocs.io/en/latest/
There is also a slack, that is generally more helpful than the docs
just note that sometimes it can take a bit to get a response: https://lab.js.org/resources/support/

To run:
Open the experiment in lab.js. 
Note: the lab.js builder does have cookies, so you don't need to re-open the project if no edits were made to it else where
To run the experiment, click the blue play button. 
The lab will open in another window. You can access the cvs at any time by clicking the three lined button on the right side of the screen
Once you go through the whole experiment, you will be given the option to download data. This will save everything to a csv file.
Description of the metrics in the csv file can be found in the testingplans.docx 

To Deploy: 
Click the arrow next to the save button, then click upload to Netlify
Make a Netliy account if you don't have one already
In another tab, go to your Netlify account, go to your profile and then go to applications
Create a personal access code. Copy this code
Back in the lab.js builder paste the code into the api. You can leave the domain name blank
You can access all completed experiments from your Netlify account
Once you have data, you can collect that data by going to Data File, copy the link into the browser and then the csv will download

Other files in folder:
fullexperiment.csv
A sample fully done experiment

mousetrap.R
An R file which can create heatmaps for the mousetracking data
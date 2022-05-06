# Nao_Sportcoach
NAO from softbank robotics will help you achieve the goal of a good exercise routine, monitoring your heart rate at all times to take care of yourself. But if you do not do it with all your power, then NAO will increase the speed of the music. 

Programs you'll need:

- Reaper is a free Digital Audio Workstation (DAW), is used to module the bpm of the song through the session. Then you installed it (https://www.reaper.fm/download.php)
you must acces to Preferences » Keyboard/Multitouch » Assign keyboard shortcuts to actions or change existing shorcuts » then you search for BPM, and finally you create new shorcuts in "Decrease current project tempo 01 BPM" and "Increase current project tempo 01 BPM".

Note: In the current code are set "CTR + -" and "CTR + I" respectively. At the moment it is essential to have Reaper as the main window after you enter the participant's name and age.  

- Python 2.7 with the libraries: naoqi (http://doc.aldebaran.com/2-5/dev/python/install_guide.html), numpy, pyserial and pywin32 avaliable via pip. 

What should you change in the code?

You should change the IP of the NAO; that is returned in function IP() in movements module, and the COM port of the HXM sensor.

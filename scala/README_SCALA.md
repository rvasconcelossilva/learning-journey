# Scala

In this section I am going to save all my tests and studies using Scala. My main goal is to learn this new language with focus on using it with Spark. I will detail, in my own words, the activities that I need to learn. My studies will be based on the official website and trainings suggested by it.

https://www.scala-lang.org/

#Setting up the environment on Windows

We need to install three components: Java JDK (Java 8 or 11), sbt and install IntelliJ to be used as IDE.

Installing the JDK:

1. Download the JDK installer https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html
2. Install the JDK following the step-by-step
3. Create one new environment variable JAVA_HOME and add the value to another PATH:
	3.1. Right-Click on This Computer/My Computer and then hit Properties
	3.2. Click on Advanced systems settings
	3.3. On the Tab Advanced hit the bottom Environment Variables on the bottom of the screen
	3.4. In the Systems Variables hit the button New
	3.5. In Name type JAVA_HOME and in value the address where JDK has been installed - e.g C:\Program Files\Java\jdk-11.0.4
	3.6. Hit the button OK
	3.7. If there is a PATH variable created in the environemnt you will select it and then hit the Edit button
		3.7.1. Hit New
		3.7.2. Type %JAVA_HOME%\bin
		3.7.3. Click On OK
	3.8. If there is no PATH variable, create a new environemnt variable with this name and then follow the same steps described above.

OBS 1: On the Scala's official website is suggesting to use the JDK 8.

Installing SBT:

SBT is a build tool for Scala and the aim of this tool is to facilitate tests and deployment of your scala applications. This link has more information https://stackoverflow.com/questions/7249871/what-is-a-build-tool.
More information about it on :https://www.scala-sbt.org/index.html

1. Download the installer https://www.scala-sbt.org/download.html
2. Run installer and then follow the step-by-step

OBS 2: I am using the most updated version of SBT which is different from the official training on Scala website

Installing IntelliJ and Scala Plug in

1. Download the IDE from https://www.jetbrains.com/idea/, execute the installer and follow the step-by-step 
2. After the installation, open IntelliJ
3. Click on Configure button
4. Hit Plugins
4. Type Scala and click on Install

#Setting up the environment on Mac

I will update this document once I have completed the Functional Programming Principles in Scala, Functional Program Design, Parallel Programming and Big Data Analyses with Scala and Spark.

WELL DONE! ALL THE REQUIRED TOOLS AND FRAMEWORKS TO START DEVELOPING ON WINDOWS IN SCALA ARE READY.



	
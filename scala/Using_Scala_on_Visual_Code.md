# Installing Scala on Visual Code

# Scala 

Setting up the java 11 on Windows 10 

Assumptions: You should have downloaded and installed the JAVA 11 JDK or Older

1. Right-click on My Computer
2. Click on Advanced settings
3. Hit the button Environment Variables
4. Click on New and type JAVA_HOME
5. Then type the value C:\Program Files\Java\jdk-11.0.4


Scala Installation on Windows 10 

1. Acess the following link: https://www.scala-lang.org/download/
2. Click on Download the Scala Bu
3. Hit the button "Install"	and then just keep clicking on Next buttons untill the end of the project
4. Again access the Environment Variables and then add the below configuration:
	Variable: %SCALA_HOME% Value: C:\Program Files (x86)\scala
	Variable: %PATH% Value: %PATH%;%SCALA_HOME%\bin

Test your Installation

1. Open VS Code and create your new Workspace
2. Add a file HellowWorld.scala
3. Copy and paste the below code:
object HelloWorld extends App {
  println("Hello, world!")
}
4. Add a folder Outputs
5. Execute the command: scalac -d outputs HelloWorld.scala to compile the below code in the output folder (it should have already been created)
6. Execute the command: scala -cp outputs HelloWorld and the output should be "Hello, world!" 

Find out more information at: https://www.scala-lang.org/documentation/your-first-lines-of-scala.html	

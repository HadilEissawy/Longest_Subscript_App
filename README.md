To run the docker file with the containarized application
open cmd, powershell in your Host 
make sure docker and python is available through your commandLine/console/terminal 
Step 1: Navigate to the directory conatining the docker image.
     cd <directory>
Step 2: Build the docker image(locally): 
     docker build -t <name of conatiner image> .
     Example: docker build -t longest-subdir-image .
     longest-subdir-image: The name of the container image that is created, you can name it as you wish. 
Step 3 : Run the conatiner image: 
     docker run --rm -v "Required_Path:/<directest>" longest-subdir-finder /"<directest>"
     directest: The path in the container that maps the path required to be tested.
      The ouput should show up in your commandline. 
      Example :  docker run --rm -v "C:\Users\Hadil Hesham\.docker:/testdir" longest-subdir-image /testdir 


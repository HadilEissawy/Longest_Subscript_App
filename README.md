To run the docker file with the containarized application
open cmd, powershell in your Host 
make sure docker and python is available through your commandLine/console/terminal 
to build the docker image: 
     docker build -t longest-subdir-image .
     longest-subdir-finder: The name of the container image that is created 
to run the conatiner image: 
     docker run --rm -v "Required_Path:/<directest>" longest-subdir-finder /"<directest>"
     directest: The path in the container that maps the path required to be tested.
      The ouput should show up in your commandline. 

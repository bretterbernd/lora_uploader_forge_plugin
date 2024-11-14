This is a simple plugin for ForgeUI / A1111 to upload LoRa files to the common directory. This is quiet a first attempt that runs ok, so improvements have to be done!

FOR DOCKERS!
for running it in Docker files, you need to create the hosting directory in the docker first an that get the files and move them:

# Create the lora_uploader_plugin folder inside extensions
RUN mkdir -p extensions/lora_uploader_plugin

# Clone the lora_uploader_plugin repository into the new folder
RUN git clone https://github.com/bretterbernd/lora_uploader_forge_plugin.git extensions/lora_uploader_plugin


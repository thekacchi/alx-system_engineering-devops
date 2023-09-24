HOW TO UPLOAD FILES USING SFTP

To use the `sftp` command to upload images to a remote server, follow these steps:

1. **Open a Terminal**: Open a terminal window on your local computer. You can usually find Terminal on macOS and Linux, or you can use an SSH client like PuTTY on Windows.

2. **Connect to the Remote Server**: Use the `sftp` command followed by the username and hostname (or IP address) of the remote server. For example:

   ```
   sftp username@hostname_or_ip
   ```

   Replace `username` with your actual username and `hostname_or_ip` with the remote server's hostname or IP address. You will be prompted to enter your password for the remote server.

3. **Navigate to the Local Directory**: Use the `cd` command to navigate to the directory on your local computer where the images are located. For example:

   ```
   cd /path/to/local/images
   ```

   Replace `/path/to/local/images` with the actual path to your image files.

4. **Navigate to the Remote Directory**: Use the `cd` command again, but this time navigate to the directory on the remote server where you want to upload the images. For example:

   ```
   cd /path/to/remote/upload/directory
   ```

   Replace `/path/to/remote/upload/directory` with the actual path on the remote server.

5. **Upload Images**: To upload images, simply use the `put` command followed by the names of the image files you want to upload. For example:

   ```
   put image1.jpg image2.png
   ```

   Replace `image1.jpg` and `image2.png` with the actual filenames of your image files. You can specify multiple filenames separated by spaces.

6. **Exit `sftp`**: Once you've uploaded your images, you can exit the `sftp` session by typing:

   ```
   exit
   ```

   This will return you to your local terminal.

Your images should now be uploaded to the specified directory on the remote server. Make sure you have the necessary permissions to write to the remote directory.

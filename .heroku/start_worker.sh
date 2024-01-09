set -e

## Added by Krishna Kollu to fix issue with Metecho not being able to execute Selenium in a subprocess that replaces the HOME variable
# Check if GOOGLE_CHROME_SHIM is set
if [ -z "$GOOGLE_CHROME_SHIM" ]; then
  echo "GOOGLE_CHROME_SHIM is not set. Exiting."
  exit 1
fi
# Check if the file exists
if [ ! -f "$GOOGLE_CHROME_SHIM" ]; then
  echo "File at $GOOGLE_CHROME_SHIM does not exist. Exiting."
  exit 1
fi
# Replace $HOME with its actual value in the file. This is needed to prevent issues with running chromium.
sed -i "s|\$HOME|${HOME}|g" "$GOOGLE_CHROME_SHIM"
# Copy this to the default google chrome file
dir=$(dirname "$GOOGLE_CHROME_SHIM")
new_file_path="$dir/google-chrome"
cp "$GOOGLE_CHROME_SHIM" "$new_file_path"
cat $GOOGLE_CHROME_SHIM
cat $new_file_path
echo "Changed Chrome SHIMS"

# make Chrome available to VBT
# Copied from https://github.com/SFDO-Tooling/MetaDeploy/pull/3468

# todo - uncomment this after issue is resolved
#mkdir -p /opt/google/chrome
#ln -s /app/.apt/usr/bin/google-chrome /opt/google/chrome/chrome
python manage.py rqworker default  

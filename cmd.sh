cd "$HOME/dev/sapienz"
if [ -z "$1" ]; then
  echo "No apk given! Aborting..."
  exit 2
fi

while [ -n "$1" ]; do
  if [ ! -f "$1" ]; then
    echo "No such file $1."
    exit 1
  fi

  rm -rf "${1}_output"
  killall -9 qemu-system-i386

  python2 -B main.py "$1"

  shift
done

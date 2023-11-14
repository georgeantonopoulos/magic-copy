# magic-copy

A simple tool for copying Nuke nodes over the network from a common server location.

## Installation

Insert the following in the `menu.py` or menu setup script:

```python
# Magic Paste Network Setup
import magic_copy
nuke.menu('Nuke').addCommand('Magic Copy/Magic Copy', "magic_copy.copy()", 'ctrl+alt+c')
nuke.menu('Nuke').addCommand('Magic Copy/Magic Paste', "magic_copy.paste()", 'ctrl+alt+v')
```

This script will add the 'Magic Copy' and 'Magic Paste' commands to the Nuke menu under 'Magic Copy', with keyboard shortcuts for easy access.

## Configuration

To configure `magic-copy`, set the 'server location' to a network path that has read/write access for all artists. This can be done by modifying the `PATH` variable in the `magic_copy` module:

```python
PATH = os.environ.get('NUKE_MAGIC_COPY_PATH', '<your-network-path-here>')
```

Replace `<your-network-path-here>` with the actual network path ensuring it is accessible to all team members.
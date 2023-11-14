# magic-copy

A simple tool for copying Nuke nodes over the network from a common server location.

## Installation

Insert the following in the `menu.py` or menu setup script:

```python
# Magic Paste Network Setup
import magic_copy
nuke.menu('Nuke').addCommand('Magic Copy/Magic Copy', "magic_copy.copy()", 'ctrl+alt+c')
nuke.menu('Nuke').addCommand('Magic Copy/Magic Paste', "magic_copy.paste()", 'ctrl+alt+v')
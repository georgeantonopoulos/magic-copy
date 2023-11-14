import nuke
import logging
import os


# Server location for the magic copy and paste.
# Choose a path that all users have access to read and write to.
PATH = os.environ.get('NUKE_MAGIC_COPY_PATH', 'server location')

def copy():
    """
    Copies the selected nodes to a predefined network location.
    """
    try:
        nuke.nodeCopy(PATH)
    except Exception as e:
        logging.error(f"Failed to copy nodes: {e}")

def paste():
    """
    Pastes nodes from a predefined network location.
    """
    try:
        nuke.nodePaste(PATH)
    except Exception as e:
        logging.error(f"Failed to paste nodes: {e}")

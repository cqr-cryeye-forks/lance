import logging
import re

class ColorizingStreamHandler(logging.StreamHandler):
    color_map = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
    }

    level_map = {
        logging.DEBUG: (None, 'blue', False),
        logging.INFO: (None, 'green', False),
        logging.WARNING: (None, 'yellow', False),
        logging.ERROR: (None, 'red', False),
        logging.CRITICAL: ('red', 'white', False)
    }
    csi = '\x1b['
    reset = '\x1b[0m'
    disable_coloring = False

    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty() and not self.disable_coloring

    def emit(self, record):
        try:
            message = self.format(record)
            stream = self.stream

            if not self.is_tty:
                if message and message[0] == "\r":
                    message = message[1:]
                stream.write(message)
            else:
                self.output_colorized(message)
            stream.write(getattr(self, 'terminator', '\n'))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except IOError:
            pass
        except Exception:
            self.handleError(record)

    def output_colorized(self, message):
        self.stream.write(message)

    def colorize(self, message, record):
        if record.levelno in self.level_map and self.is_tty:
            bg, fg, bold = self.level_map[record.levelno]
            params = []

            if bg in self.color_map:
                params.append(str(self.color_map[bg] + 40))

            if fg in self.color_map:
                params.append(str(self.color_map[fg] + 30))

            if bold:
                params.append('1')

            if params and message:
                prefix = re.match(r"\s*", message).group(0)
                message = message[len(prefix):]
                message = f"{prefix}{self.csi}{';'.join(params)}m{message}{self.reset}"

        return message

    def format(self, record):
        message = logging.StreamHandler.format(self, record)
        return self.colorize(message, record)
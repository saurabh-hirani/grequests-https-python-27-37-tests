import logging


def get_hostname():
    import subprocess
    p = subprocess.Popen(['cat', '/etc/hostname'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = p.communicate()
    if p.returncode != 0:
        return ''
    return out.decode("utf-8").strip()


def setup_logging(log_level):
    """ Logger setup """
    global logger
    logger = logging.getLogger()

    log_level = getattr(logging, log_level)
    logger.setLevel(log_level)

    logHandler = logging.StreamHandler()

    hostname = get_hostname()

    logging_format = ''

    # long log format
    # logging_format_pre = '%(asctime)s '

    # short log format
    logging_format_pre = ''

    logging_format += logging_format_pre
    if hostname != '':
        # long log format
        # logging_format += ' - ' + hostname + ' - '

        # short log format
        logging_format += hostname + ' - '
    else:
        # long log format
        # logging_format += ''

        # short log format
        logging_format += 'localhost - '

    # long log format
    # logging_format_post = '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s - %(message)s'

    # short log format
    logging_format_post = '%(message)s'

    logging_format += logging_format_post

    formatter = logging.Formatter(logging_format)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    return logger

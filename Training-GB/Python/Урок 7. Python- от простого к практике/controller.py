import import_data
import export_data
import input
import log


def start():
    if input.mod() == '1':
        info = input.exp()
        export_data.expp(info)
        log.log_info(info)
    else:
        info = input.inpp()
        import_data.impo(info)
        log.log_info(info)
        

def patch_all():
  import blocking_socket
  import non_blocking_socket
  blocking_socket.socket = non_blocking_socket.socket


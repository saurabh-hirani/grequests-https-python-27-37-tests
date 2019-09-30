def patch_all():
  import mysocket
  import patched_socket
  mysocket.f1 = patched_socket.f1

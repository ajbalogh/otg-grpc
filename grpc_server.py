"""GRPC server
- registers a gNMI service
- starts the server as a daemon
"""
import threading
from concurrent import futures
import grpc
import otg_service
import argparse


class GrpcServer(object):
    """A grpc server that exposes the `IxNetwork Open Traffic Generator Service`
    """
    def __init__(self, address='[::]:5005'):
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        otg_service.OtgService(self._server)
        self._server.add_insecure_port(address)
        self._thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        self._server.start()

    def start(self):
        self._thread.start()
        self._server.wait_for_termination()

    def stop(self):
        self._server.stop(grace=0)
        self._thread.join(timeout=10)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Start the IxNetwork open traffic generator service')
    parser.add_argument('--demo',
                        action='store_true',
                        help='Demo mode that returns default metrics')
    parser.add_argument(
        '--address',
        type=str,
        default='[::]:5050',
        help='Listening address, default ADDRESS is localhost:5050')
    args = parser.parse_args()
    # start the grpc service
    server = GrpcServer(address=args.address)
    server.start()

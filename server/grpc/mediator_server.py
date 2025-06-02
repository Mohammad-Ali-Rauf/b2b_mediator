import grpc
from concurrent import futures
import time

from server.grpc import mediator_pb2
from server.grpc import mediator_pb2_grpc

# Placeholder: You’ll wire this to your real mediation logic later
def fake_ai_response(audio_chunk: bytes, user_id: str):
    print(f"[DEBUG] Got audio from {user_id} — {len(audio_chunk)} bytes")

    return mediator_pb2.MediationResponse( # type: ignore
        agent_id="mediator_ai_01",
        text="Please remain calm and continue respectfully.",
        audio=b"\x00\x01\x02",  # Fake audio bytes — replace with real TTS later
        emotion=mediator_pb2.CALM, # type: ignore
        summary="Minor conflict detected. Mediation suggested."
    )

class MediatorServicer(mediator_pb2_grpc.MediatorServiceServicer):
    def Mediate(self, request_iterator, context):
        for voice_chunk in request_iterator:
            print(f"[INFO] Streaming from user {voice_chunk.user_id}")
            response = fake_ai_response(voice_chunk.audio_chunk, voice_chunk.user_id)
            yield response

    def Ping(self, request, context):
        return mediator_pb2.Status(message="Mediator is alive and vibing 🧘‍♂️") # type: ignore

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # type: ignore
    mediator_pb2_grpc.add_MediatorServiceServicer_to_server(MediatorServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("🚀 Mediator gRPC server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("🛑 Shutting down server...")
        server.stop(0)

if __name__ == "__main__":
    serve()
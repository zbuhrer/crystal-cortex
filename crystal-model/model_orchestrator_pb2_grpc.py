# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import model_orchestrator_pb2 as model__orchestrator__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in model_orchestrator_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ModelOrchestratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessText = channel.unary_unary(
                '/model_orchestrator.ModelOrchestrator/ProcessText',
                request_serializer=model__orchestrator__pb2.ProcessTextRequest.SerializeToString,
                response_deserializer=model__orchestrator__pb2.ProcessTextResponse.FromString,
                _registered_method=True)
        self.GenerateEmbedding = channel.unary_unary(
                '/model_orchestrator.ModelOrchestrator/GenerateEmbedding',
                request_serializer=model__orchestrator__pb2.GenerateEmbeddingRequest.SerializeToString,
                response_deserializer=model__orchestrator__pb2.GenerateEmbeddingResponse.FromString,
                _registered_method=True)
        self.LoadModel = channel.unary_unary(
                '/model_orchestrator.ModelOrchestrator/LoadModel',
                request_serializer=model__orchestrator__pb2.LoadModelRequest.SerializeToString,
                response_deserializer=model__orchestrator__pb2.LoadModelResponse.FromString,
                _registered_method=True)
        self.UnloadModel = channel.unary_unary(
                '/model_orchestrator.ModelOrchestrator/UnloadModel',
                request_serializer=model__orchestrator__pb2.UnloadModelRequest.SerializeToString,
                response_deserializer=model__orchestrator__pb2.UnloadModelResponse.FromString,
                _registered_method=True)
        self.GetPrediction = channel.unary_unary(
                '/model_orchestrator.ModelOrchestrator/GetPrediction',
                request_serializer=model__orchestrator__pb2.GetPredictionRequest.SerializeToString,
                response_deserializer=model__orchestrator__pb2.GetPredictionResponse.FromString,
                _registered_method=True)


class ModelOrchestratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateEmbedding(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnloadModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPrediction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelOrchestratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessText': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessText,
                    request_deserializer=model__orchestrator__pb2.ProcessTextRequest.FromString,
                    response_serializer=model__orchestrator__pb2.ProcessTextResponse.SerializeToString,
            ),
            'GenerateEmbedding': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateEmbedding,
                    request_deserializer=model__orchestrator__pb2.GenerateEmbeddingRequest.FromString,
                    response_serializer=model__orchestrator__pb2.GenerateEmbeddingResponse.SerializeToString,
            ),
            'LoadModel': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadModel,
                    request_deserializer=model__orchestrator__pb2.LoadModelRequest.FromString,
                    response_serializer=model__orchestrator__pb2.LoadModelResponse.SerializeToString,
            ),
            'UnloadModel': grpc.unary_unary_rpc_method_handler(
                    servicer.UnloadModel,
                    request_deserializer=model__orchestrator__pb2.UnloadModelRequest.FromString,
                    response_serializer=model__orchestrator__pb2.UnloadModelResponse.SerializeToString,
            ),
            'GetPrediction': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPrediction,
                    request_deserializer=model__orchestrator__pb2.GetPredictionRequest.FromString,
                    response_serializer=model__orchestrator__pb2.GetPredictionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'model_orchestrator.ModelOrchestrator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('model_orchestrator.ModelOrchestrator', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ModelOrchestrator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/model_orchestrator.ModelOrchestrator/ProcessText',
            model__orchestrator__pb2.ProcessTextRequest.SerializeToString,
            model__orchestrator__pb2.ProcessTextResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GenerateEmbedding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/model_orchestrator.ModelOrchestrator/GenerateEmbedding',
            model__orchestrator__pb2.GenerateEmbeddingRequest.SerializeToString,
            model__orchestrator__pb2.GenerateEmbeddingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LoadModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/model_orchestrator.ModelOrchestrator/LoadModel',
            model__orchestrator__pb2.LoadModelRequest.SerializeToString,
            model__orchestrator__pb2.LoadModelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UnloadModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/model_orchestrator.ModelOrchestrator/UnloadModel',
            model__orchestrator__pb2.UnloadModelRequest.SerializeToString,
            model__orchestrator__pb2.UnloadModelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPrediction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/model_orchestrator.ModelOrchestrator/GetPrediction',
            model__orchestrator__pb2.GetPredictionRequest.SerializeToString,
            model__orchestrator__pb2.GetPredictionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

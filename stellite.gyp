# Copyright 2016 LINE Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'variables': {
    'chromium_code': 1,
    'intermediate_dir': '',
  },
  'targets': [
    {
      'target_name': 'stellite_base',
      'type': '<(component)',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
      ],
      'sources': [
        'synchronization/rwlock.h',
        'synchronization/rwlock.cc',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'logging_base',
      'type': '<(component)',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:net',
      ],
      'sources': [
        'logging/file_switch.cc',
        'logging/file_switch.h',
        'logging/file_switch_per_date.cc',
        'logging/file_switch_per_date.h',
        'logging/log_file.h',
        'logging/log_file_factory.h',
        'logging/log_file_factory_default.cc',
        'logging/log_file_factory_default.h',
        'logging/log_file_posix.cc',
        'logging/log_file_posix.h',
        'logging/log_file_writer.cc',
        'logging/log_file_writer.h',
        'logging/logging.cc',
        'logging/logging.h',
        'logging/logging_service.cc',
        'logging/logging_service.h',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'quic_server_base',
      'type': '<(component)',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '<(DEPTH)/components/components.gyp:url_matcher',
        '<(DEPTH)/crypto/crypto.gyp:crypto',
        '<(DEPTH)/ipc/ipc.gyp:ipc',
        '<(DEPTH)/net/net.gyp:net',
        '<(DEPTH)/net/net.gyp:net_quic_proto',
        '<(DEPTH)/third_party/re2/re2.gyp:re2',
        '<(DEPTH)/url/url.gyp:url_lib',
        'stellite_base',
      ],
      'sources': [
        'crypto/quic_ephemeral_key_source.cc',
        'crypto/quic_ephemeral_key_source.h',
        'crypto/quic_signature_creator.h',
        'fetcher/http_fetcher.cc',
        'fetcher/http_fetcher.h',
        'fetcher/http_fetcher_core.cc',
        'fetcher/http_fetcher_core.h',
        'fetcher/http_fetcher_impl.cc',
        'fetcher/http_fetcher_impl.h',
        'fetcher/http_fetcher_task.cc',
        'fetcher/http_fetcher_task.h',
        'fetcher/http_request_context_getter.cc',
        'fetcher/http_request_context_getter.h',
        'fetcher/http_rewrite.cc',
        'fetcher/http_rewrite.h',
        'fetcher/spdy_utils.cc',
        'fetcher/spdy_utils.h',
        'process/daemon.cc',
        'process/daemon.h',
#        'server/http_stats_server.cc',
#        'server/http_stats_server.h',
        'server/parse_util.cc',
        'server/parse_util.h',
        'server/proxy_stream.cc',
        'server/proxy_stream.h',
        'server/quic_thread_server.cc',
        'server/quic_thread_server.h',
        'server/server_config.cc',
        'server/server_config.h',
        'server/server_packet_writer.cc',
        'server/server_packet_writer.h',
        'server/server_per_connection_packet_writer.cc',
        'server/server_per_connection_packet_writer.h',
        'server/server_session.cc',
        'server/server_session.h',
        'server/thread_dispatcher.cc',
        'server/thread_dispatcher.h',
        'server/thread_worker.cc',
        'server/thread_worker.h',
        'socket/quic_udp_server_socket.cc',
        'socket/quic_udp_server_socket.h',
        'socket/quic_udp_socket.h',
        'socket/quic_udp_socket_posix.cc',
        'socket/quic_udp_socket_posix.h',
        'stats/server_stats.cc',
        'stats/server_stats.h',
        'stats/server_stats_macro.h',
        'stats/server_stats_recorder.cc',
        'stats/server_stats_recorder.h',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'quic_thread_server',
      'type': 'executable',
      'sources': [
        'quic_thread_server_main.cc',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:http_server',
        '<(DEPTH)/net/net.gyp:net',
        '<(DEPTH)/net/net.gyp:net_quic_proto',
        '<(DEPTH)/net/net.gyp:simple_quic_tools',
        'logging_base',
        'quic_server_base',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'stellite_client_base_private',
      'type': '<(component)',
      'sources': [
        'client/backend_cache.cc',
        'client/backend_cache.h',
        'client/backend_factory.cc',
        'client/backend_factory.h',
        'client/cache_based_quic_server_info.cc',
        'client/cache_based_quic_server_info.h',
        'client/cache_based_quic_server_info_factory.cc',
        'client/cache_based_quic_server_info_factory.h',
        'client/contents_filter_context.cc',
        'client/contents_filter_context.h',
        'client/network_transaction_client.cc',
        'client/network_transaction_client.h',
        'client/network_transaction_consumer.cc',
        'client/network_transaction_consumer.h',
        'client/network_transaction_factory.cc',
        'client/network_transaction_factory.h',
        'client/http_ssl_config_service.cc',
        'client/http_ssl_config_service.h',
        'client/http_client_impl.cc',
        'client/http_client_impl.h',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:net',
        '<(DEPTH)/url/url.gyp:url_lib',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'stellite_client_base',
      'type': '<(component)',
      'sources': [
        'client/http_client_context.cc',
        'client/http_request.cc',
        'client/http_response.cc',
        'client/logging.cc',
        'include/http_client.h',
        'include/http_client_context.h',
        'include/http_request.h',
        'include/http_response.h',
        'include/logging.h',
        'include/stellite_export.h',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:net',
        '<(DEPTH)/url/url.gyp:url_lib',
        'stellite_client_base_private',
      ],
      'defines': [
        'STELLITE_IMPLEMENTATION',
        'COMPONENT_BUILD',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'stellite_http_client_bin',
      'type': 'executable',
      'sources': [
        'http_client_bin.cc',
      ],
      'dependencies': [
        'stellite_client_base',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:net',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'stellite_unittests',
      'type': '<(gtest_target_type)',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/base/base.gyp:test_support_base',
        '<(DEPTH)/net/net.gyp:net',
        '<(DEPTH)/net/net.gyp:net_quic_proto',
        '<(DEPTH)/net/net.gyp:net_test_support',
        '<(DEPTH)/net/net.gyp:simple_quic_tools',
        '<(DEPTH)/testing/gmock.gyp:gmock',
        '<(DEPTH)/testing/gtest.gyp:gtest',
        'logging_base',
        'stellite_client_base',
        'quic_server_base',
      ],
      'sources': [
        'client/alternative_service_unittest.cc',
        'client/http_client_context_unittest.cc',
        'client/http_client_unittest.cc',
        'client/http_request_unittest.cc',
        'client/http_response_unittest.cc',
        'client/logging_unittest.cc',
        'fetcher/http_fetcher_unittest.cc',
        'fetcher/url_fetcher_unittest.cc',
        'integration_test/http_chunked_integration_unittest.cc',
        'integration_test/http_client_integration_unittest.cc',
        'integration_test/quic_client_end_to_end_unittest.cc',
#'integration_test/quic_connection_migration_unittest.cc',
        'integration_test/quic_discovery_unittest.cc',
        'integration_test/quic_server_alternative_service_unittest.cc',
        'integration_test/quic_server_reverse_proxy_unittest.cc',
        'integration_test/request_count_unittest.cc',
        'logging/log_file_posix_unittest.cc',
        'logging/log_file_writer_unittest.cc',
        'test/http_test_server.cc',
        'test/http_test_server.h',
        'test/quic_mock_server.cc',
        'test/quic_mock_server.h',
        'test/quic_test_suite.cc',
        'test/quic_test_suite.h',
        'test/run_all_unittests.cc',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'http_stability_test',
      'type': 'executable',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/base/base.gyp:test_support_base',
        '<(DEPTH)/net/net.gyp:net',
        '<(DEPTH)/net/net.gyp:net_quic_proto',
        '<(DEPTH)/net/net.gyp:net_test_support',
        '<(DEPTH)/net/net.gyp:simple_quic_tools',
        'stellite_client_base',
        'quic_server_base',
      ],
      'sources': [
        'test/http_test_server.cc',
        'test/http_test_server.h',
        'test/quic_mock_server.cc',
        'test/quic_mock_server.h',
        'test_tools/http_stability_test.cc',
      ],
    },
    {
      'target_name': 'stellite_client_binder',
      'type': 'shared_library',
      'dependencies': [
        'stellite_client_base',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:net',
      ],
      'sources': [
        'stub/client_binder.h',
        'stub/client_binder.cc',
      ],
      'defines': [
        'STELLITE_IMPLEMENTATION',
        'COMPONENT_BUILD',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],
    },
    {
      'target_name': 'stability_test_client',
      'type': 'executable',
      'dependencies': [
        'stellite_client_base',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:net',
      ],
      'sources': [
        'test/stability_test_client.cc',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '..',
      ],

    }
  ],
}

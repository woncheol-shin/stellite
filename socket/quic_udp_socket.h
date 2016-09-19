// Copyright 2016 LINE Corporation
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef STELLITE_SOCKET_QUIC_UDP_SOCKET_H_
#define STELLITE_SOCKET_QUIC_UDP_SOCKET_H_

#include "build/build_config.h"

#if defined(OS_WIN)
#include "net/udp/udp_socket_win.h"
#elif defined(OS_POSIX)
#include "stellite/socket/quic_udp_socket_posix.h"
#endif

namespace net {

#if defined(OS_WIN)
typedef UDPSocketWin QuicUDPSocket;
#elif defined(OS_POSIX)
typedef QuicUDPSocketPosix QuicUDPSocket;
#endif

}  // namespace net

#endif  // STELLITE_SOCKET_QUIC_UDP_SOCKET_H_

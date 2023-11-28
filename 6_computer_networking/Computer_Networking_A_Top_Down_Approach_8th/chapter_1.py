introduction = """

network edge : hosts, access network, physical media
network core : packet/circuit switching, internet structure
performance : loss, delay, throughput
protocol layers, service models


CONNECTED DEVICES:
    host = end systems
    edge = app
        internet-connected devices

PACKET SWITCHES: forward packets
    routers, switches 

COMMUNICATION LINKS:
    fiber, copper, radio, satellite
    transmission rate : bandwidth

NETWORK
    collection of devices, routers, links: managed by an organization

"""

what_is_network = """
view of nuts and bolts
- network of network
- protocols are everywhere
- internet standards

view of services
- that provides services to applications
- provides programming interface to distributed applications 
"""

internet_structure = """
network edge
    - hosts: clients and servers
    - servers often in data centers
network access
    - wired, wireless communication links
network core
    - interconnected routers
    - network of networks
"""

how_to_connect_end_systems_to_edge_router = """
- residential access nets
- institutional access networks (school, company)
- mobile access networks (WiFi, 4G/5G)

-> transmission rate of access network
-> SHARED OR DEDICATED
"""

access_networks = """
다양하게도 연결되어있다
DSL : 기존 전화선 이용
Cable : network 만을 위한 선

어쨌거나 shared cable로부터 cable_headend로 귀결됨
"""

wireless_access_networks = """
WLANS
wireless local area networks (집 내부)

Wide-Area Cellular access networks
5g 같은거
"""

enterprise_networks = """
mixed
"""

data_center_networks = """
뭐 그런게 있다.
"""

HOST = """
takes application message
sends packets of data

어플리케이션의 메시지를 받아 페킷을 보내는 주체

P acket to
L ength with
R ate of transmission

packet_transmission_delay = L / R
"""

LINKS = """
phisical media

bit : transmitter랑 redeiver 사이에 지나다니는 뭔가 뭔가들
physical links : receiver랑 transmitter 사이에 깔린 뭔가들
guided media : 구리나 광 케이블 같이 정해진 것 내로만 다니는 신호
unguided media : radio같이 걍 뿌려지는거

(twisted pairs) 는.. 랜선.. 꼬여있어서 걍 이렇게 부르는 듯
(coaxial cable) 는 동축 케이블..
(fiber cable) 는 광 케이블
radio links 는 4g나 wifi, 블투, 위성 신호 모두 포함
"""

NETWORK_EDGE = [
    how_to_connect_end_systems_to_edge_router,
    access_networks,
    wireless_access_networks,
    enterprise_networks,
    data_center_networks,
    HOST,
    LINKS
]

network_core_two_function = """
1. swithing : switching table을 보고 어디로 보내는지 확인
2. routing : global action이다. 어디로 가야할지 route 해주는 것
네비게이션 기능 같은 것

local_forwarding(Swithing)
global_routing

store and forwarding (속도가 느려질 경우)
큐잉 해서 차례로 보내버린다..

패킷은 드랍될 수 있다.. 라우터 내의 버퍼가 꽉 찬 경우..

"""

alternative_to_packet_Switching_is_circuit_switching = """
패킷 구간에 유저가 4명 있는데요 이걸..
FDM Frequency로 나눈다
TDM Time으로 나눈다

그럼 1G 링크에
각 유저가
active일때 100Mb 먹고
10% active 타밍일경우

circuit switching 인 경우 10명
packet switching 인 경우 35명 이상 쓸 수 있으나.. loss가 생길 수 있다
무조건 도착한다는 보장이 없다..

circuit switching은 circuit을 어떻게 짜느냐에 따라 달렸다
(이건 요즘 아무도 안씀)
"""

network_of_networks = """
여러가지가 매우 복잡하게 얽혀있는게 또 복잡하게 연결되어있다 그 말입니다!
그럼 뭘로 연결을 보장하냐

ISP를 통해서 조금 보장한다..
Internet Service Provider

ISP 사이에도 IXP를 둬서 ISP간의 통신을 보장함(exchange point)
그런데 그 사이에 peer link 를 통해서 직접 연결하는 경우도 있고
블라 블라 암튼 다양한 경로를 통해서 다양하게 연결되어있다.
"""

NETWORK_CORE = [
    network_core_two_function,
    alternative_to_packet_Switching_is_circuit_switching,
    network_of_networks,
]

OID: 1.3.6.1.2.1.1.1
Name: sysDescr(1)
Description: sysDescr OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A textual description of the entity. This value should  include the full name and version identification of  the system's hardware type, software operating-system,  and networking software."
----------------------------------------
OID: 1.3.6.1.2.1.1.2
Name: sysObjectID(2)
Description: sysObjectID OBJECT-TYPE  SYNTAX OBJECT IDENTIFIER  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The vendor's authoritative identification of the  network management subsystem contained in the entity.  This value is allocated within the SMI enterprises  subtree (1.3.6.1.4.1) and provides an easy and  unambiguous means for determining `what kind of box' is  being managed. For example, if vendor `Flintstones,  Inc.' was assigned the subtree 1.3.6.1.4.1.424242,  it could assign the identifier 1.3.6.1.4.1.424242.1.1  to its `Fred Router'."
----------------------------------------
OID: 1.3.6.1.2.1.1.3
Name: sysUpTime(3)
Description: sysUpTime OBJECT-TYPE  SYNTAX TimeTicks  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The time (in hundredths of a second) since the  network management portion of the system was last  re-initialized."
----------------------------------------
OID: 1.3.6.1.2.1.1.4
Name: sysContact(4)
Description: sysContact OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The textual identification of the contact person for  this managed node, together with information on how  to contact this person. If no contact information is  known, the value is the zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.1.5
Name: sysName(5)
Description: sysName OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "An administratively-assigned name for this managed  node. By convention, this is the node's fully-qualified  domain name. If the name is unknown, the value is  the zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.1.6
Name: sysLocation(6)
Description: sysLocation OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The physical location of this node (e.g., 'telephone  closet, 3rd floor'). If the location is unknown, the  value is the zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.1.7
Name: sysServices(7)
Description: sysServices OBJECT-TYPE  SYNTAX INTEGER (0..127)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A value which indicates the set of services that this  entity may potentially offer. The value is a sum.  This sum initially takes the value zero. Then, for  each layer, L, in the range 1 through 7, that this node  performs transactions for, 2 raised to (L - 1) is added  to the sum. For example, a node which performs only  routing functions would have a value of 4 (2^(3-1)).  In contrast, a node which is a host offering application  services would have a value of 72 (2^(4-1) + 2^(7-1)).  Note that in the context of the Internet suite of  protocols, values should be calculated accordingly:  layer functionality  1 physical (e.g., repeaters)  2 datalink/subnetwork (e.g., bridges)  3 internet (e.g., supports the IP)  4 end-to-end (e.g., supports the TCP)  7 applications (e.g., supports the SMTP)  For systems including OSI protocols, layers 5 and 6  may also be counted."
----------------------------------------
OID: 1.3.6.1.2.1.2.1
Name: ifNumber(1)
Description: ifNumber OBJECT-TYPE  SYNTAX INTEGER  ACCESS read-only  STATUS mandatory  DESCRIPTION  "The number of network interfaces (regardless of their current state) present on this system."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.1
Name: ifIndex(1)
Description: ifIndex OBJECT-TYPE  SYNTAX InterfaceIndex  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A unique value, greater than zero, for each interface. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.2
Name: ifDescr(2)
Description: ifDescr OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A textual string containing information about theinterface. This string should include the name of the manufacturer, the product name and the version of the interface hardware/software."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.3
Name: ifType(3)
Description: N/A
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.4
Name: ifMtu(4)
Description: ifMtu OBJECT-TYPE  SYNTAX Integer32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The size of the largest packet which can be sent/received on the interface, specified in octets. For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.5
Name: ifSpeed(5)
Description: ifSpeed OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An estimate of the interface's current bandwidth in bits  per second. For interfaces which do not vary in bandwidth  or for those where no accurate estimation can be made, this  object should contain the nominal bandwidth. If the  bandwidth of the interface is greater than the maximum value  reportable by this object then this object should report its  maximum value (4,294,967,295) and ifHighSpeed must be used  to report the interace's speed. For a sub-layer which has  no concept of bandwidth, this object should be zero."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.6
Name: ifPhysAddress(6)
Description: ifPhysAddress OBJECT-TYPE  SYNTAX PhysAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The interface's address at its protocol sub-layer. For  example, for an 802.x interface, this object normally  contains a MAC address. The interface's media-specific MIB  must define the bit and byte ordering and the format of the  value of this object. For interfaces which do not have such  an address (e.g., a serial line), this object should contain  an octet string of zero length."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.7
Name: ifAdminStatus(7)
Description: ifAdminStatus OBJECT-TYPE  SYNTAX INTEGER {  up(1), -- ready to pass packets  down(2),  testing(3) -- in some test mode  }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The desired state of the interface. The testing(3) state  indicates that no operational packets can be passed. When a  managed system initializes, all interfaces start with  ifAdminStatus in the down(2) state. As a result of either  explicit management action or per configuration information  retained by the managed system, ifAdminStatus is then  changed to either the up(1) or testing(3) states (or remains  in the down(2) state)."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.8
Name: ifOperStatus(8)
Description: ifOperStatus OBJECT-TYPE  SYNTAX INTEGER {  up(1), -- ready to pass packets  down(2),  testing(3), -- in some test mode  unknown(4), -- status can not be determined  -- for some reason.  dormant(5),  notPresent(6), -- some component is missing  lowerLayerDown(7) -- down due to state of  -- lower-layer interface(s)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The current operational state of the interface. The  testing(3) state indicates that no operational packets can  be passed. If ifAdminStatus is down(2) then ifOperStatus  should be down(2). If ifAdminStatus is changed to up(1)  then ifOperStatus should change to up(1) if the interface is  ready to transmit and receive network traffic; it should  change to dormant(5) if the interface is waiting for  external actions (such as a serial line waiting for an  incoming connection); it should remain in the down(2) state  if and only if there is a fault that prevents it from going  to the up(1) state; it should remain in the notPresent(6)  state if the interface has missing (typically, hardware)  components."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.9
Name: ifLastChange(9)
Description: ifLastChange OBJECT-TYPE  SYNTAX TimeTicks  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime at the time the interface entered  its current operational state. If the current state was  entered prior to the last re-initialization of the local  network management subsystem, then this object contains a  zero value."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.10
Name: ifInOctets(10)
Description: ifInOctets OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received on the interface,  including framing characters.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.11
Name: ifInUcastPkts(11)
Description: ifInUcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were not addressed to a multicast  or broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.12
Name: ifInNUcastPkts(12)
Description: ifInNUcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a multicast or  broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime.  This object is deprecated in favour of ifInMulticastPkts and  ifInBroadcastPkts."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.13
Name: ifInDiscards(13)
Description: ifInDiscards OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of inbound packets which were chosen to be  discarded even though no errors had been detected to prevent  their being deliverable to a higher-layer protocol. One  possible reason for discarding such a packet could be to  free up buffer space.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.14
Name: ifInErrors(14)
Description: ifInErrors OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "For packet-oriented interfaces, the number of inbound  packets that contained errors preventing them from being  deliverable to a higher-layer protocol. For character-  oriented or fixed-length interfaces, the number of inbound  transmission units that contained errors preventing them  from being deliverable to a higher-layer protocol.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.15
Name: ifInUnknownProtos(15)
Description: ifInUnknownProtos OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "For packet-oriented interfaces, the number of packets  received via the interface which were discarded because of  an unknown or unsupported protocol. For character-oriented  or fixed-length interfaces that support protocol  multiplexing the number of transmission units received via  the interface which were discarded because of an unknown or  unsupported protocol. For any interface that does not  support protocol multiplexing, this counter will always be  0.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.16
Name: ifOutOctets(16)
Description: ifOutOctets OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets transmitted out of the  interface, including framing characters.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.17
Name: ifOutUcastPkts(17)
Description: ifOutUcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were not addressed to a  multicast or broadcast address at this sub-layer, including  those that were discarded or not sent.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.18
Name: ifOutNUcastPkts(18)
Description: ifOutNUcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  multicast or broadcast address at this sub-layer, including  those that were discarded or not sent.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime.  This object is deprecated in favour of ifOutMulticastPkts  and ifOutBroadcastPkts."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.19
Name: ifOutDiscards(19)
Description: ifOutDiscards OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of outbound packets which were chosen to be  discarded even though no errors had been detected to prevent  their being transmitted. One possible reason for discarding  such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.20
Name: ifOutErrors(20)
Description: ifOutErrors OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "For packet-oriented interfaces, the number of outbound  packets that could not be transmitted because of errors.  For character-oriented or fixed-length interfaces, the  number of outbound transmission units that could not be  transmitted because of errors.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.21
Name: ifOutQLen(21)
Description: ifOutQLen OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The length of the output packet queue (in packets)."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.22
Name: ifSpecific(22)
Description: ifSpecific OBJECT-TYPE  SYNTAX OBJECT IDENTIFIER  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "A reference to MIB definitions specific to the particular  media being used to realize the interface. It is  recommended that this value point to an instance of a MIB  object in the media-specific MIB, i.e., that this object  have the semantics associated with the InstancePointer  textual convention defined in RFC 2579. In fact, it is  recommended that the media-specific MIB specify what value  ifSpecific should/can take for values of ifType. If no MIB  definitions specific to the particular media are available,  the value should be set to the OBJECT IDENTIFIER { 0 0 }."
----------------------------------------
OID: 1.3.6.1.2.1.4.1
Name: ipForwarding(1)
Description: ipForwarding OBJECT-TYPE  SYNTAX INTEGER {  forwarding(1), -- acting as a router  notForwarding(2) -- NOT acting as a router  }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The indication of whether this entity is acting as an IPv4  router in respect to the forwarding of datagrams received  by, but not addressed to, this entity. IPv4 routers forward  datagrams. IPv4 hosts do not (except those source-routed  via the host).  When this object is written, the entity should save the  change to non-volatile storage and restore the object from  non-volatile storage upon re-initialization of the system.  Note: a stronger requirement is not used because this object  was previously defined."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.1
Name: ipAdEntAddr(1)
Description: ipAdEntAddr OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The IPv4 address to which this entry's addressing  information pertains."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.2
Name: ipAdEntIfIndex(2)
Description: ipAdEntIfIndex OBJECT-TYPE  SYNTAX INTEGER (1..2147483647)  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The index value which uniquely identifies the interface to  which this entry is applicable. The interface identified by  a particular value of this index is the same interface as  identified by the same value of the IF-MIB's ifIndex."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.3
Name: ipAdEntNetMask(3)
Description: ipAdEntNetMask OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The subnet mask associated with the IPv4 address of this  entry. The value of the mask is an IPv4 address with all  the network bits set to 1 and all the hosts bits set to 0."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.4
Name: ipAdEntBcastAddr(4)
Description: ipAdEntBcastAddr OBJECT-TYPE  SYNTAX INTEGER (0..1)  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The value of the least-significant bit in the IPv4 broadcast  address used for sending datagrams on the (logical)  interface associated with the IPv4 address of this entry.  For example, when the Internet standard all-ones broadcast  address is used, the value will be 1. This value applies to  both the subnet and network broadcast addresses used by the  entity on this (logical) interface."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.5
Name: ipAdEntReasmMaxSize(5)
Description: ipAdEntReasmMaxSize OBJECT-TYPE  SYNTAX INTEGER (0..65535)  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The size of the largest IPv4 datagram which this entity can  re-assemble from incoming IPv4 fragmented datagrams received  on this interface."
----------------------------------------
OID: 1.3.6.1.2.1.4.24.6
Name: inetCidrRouteNumber(6)
Description: inetCidrRouteNumber OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of current inetCidrRouteTable entries that  are not invalid."
----------------------------------------
OID: 1.3.6.1.2.1.4.30.1.1
Name: ipv6InterfaceIfIndex(1)
Description: ipv6InterfaceIfIndex OBJECT-TYPE  SYNTAX InterfaceIndex  MAX-ACCESS not-accessible  STATUS current  DESCRIPTION  "The index value that uniquely identifies the interface to  which this entry is applicable. The interface identified by  a particular value of this index is the same interface as  identified by the same value of the IF-MIB's ifIndex."
----------------------------------------
OID: 1.3.6.1.2.1.4.30.1.2
Name: N/A
Description: ipv6InterfaceReasmMaxSize OBJECT-TYPE  SYNTAX Unsigned32 (1500..65535)  UNITS "octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The size of the largest IPv6 datagram that this entity can  re-assemble from incoming IPv6 fragmented datagrams received  on this interface."
----------------------------------------
OID: 1.3.6.1.2.1.4.30.1.3
Name: N/A
Description: ipv6InterfaceIdentifier OBJECT-TYPE  SYNTAX Ipv6AddressIfIdentifierTC  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Interface Identifier for this interface. The Interface  Identifier is combined with an address prefix to form an  interface address.  By default, the Interface Identifier is auto-configured  according to the rules of the link type to which this  interface is attached.  A zero length identifier may be used where appropriate. One  possible example is a loopback interface."
----------------------------------------
OID: 1.3.6.1.2.1.4.30.1.5
Name: N/A
Description: ipv6InterfaceEnableStatus OBJECT-TYPE  SYNTAX INTEGER {  up(1),  down(2)  }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The indication of whether IPv6 is enabled (up) or disabled  (down) on this interface. This object does not affect the  state of the interface itself, only its connection to an  IPv6 stack. The IF-MIB should be used to control the state  of the interface.  When this object is written, the entity SHOULD save the  change to non-volatile storage and restore the object from  non-volatile storage upon re-initialization of the system."
----------------------------------------
OID: 1.3.6.1.2.1.4.30.1.6
Name: N/A
Description: ipv6InterfaceReachableTime OBJECT-TYPE  SYNTAX Unsigned32  UNITS "milliseconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The time a neighbor is considered reachable after receiving  a reachability confirmation."  REFERENCE "RFC 2461, Section 6.3.2"
----------------------------------------
OID: 1.3.6.1.2.1.4.30.1.7
Name: N/A
Description: ipv6InterfaceRetransmitTime OBJECT-TYPE  SYNTAX Unsigned32  UNITS "milliseconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The time between retransmissions of Neighbor Solicitation  messages to a neighbor when resolving the address or when  probing the reachability of a neighbor."  REFERENCE "RFC 2461, Section 6.3.2"
----------------------------------------
OID: 1.3.6.1.2.1.4.30.1.8
Name: N/A
Description: ipv6InterfaceForwarding OBJECT-TYPE  SYNTAX INTEGER {  forwarding(1), -- acting as a router  notForwarding(2) -- NOT acting as a router  }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The indication of whether this entity is acting as an IPv6  router on this interface with respect to the forwarding of  datagrams received by, but not addressed to, this entity.  IPv6 routers forward datagrams. IPv6 hosts do not (except  those source-routed via the host).  This object is constrained by ipv6IpForwarding and is  ignored if ipv6IpForwarding is set to notForwarding. Those  systems that do not provide per-interface control of the  forwarding function should set this object to forwarding for  all interfaces and allow the ipv6IpForwarding object to  control the forwarding capability.  When this object is written, the entity SHOULD save the  change to non-volatile storage and restore the object from  non-volatile storage upon re-initialization of the system."
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.1
Name: ipAddressAddrType(1)
Description: ipAddressAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS not-accessible  STATUS current  DESCRIPTION  "The address type of ipAddressAddr."
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.2
Name: ipAddressAddr(2)
Description: ipAddressAddr OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS not-accessible  STATUS current  DESCRIPTION  "The IP address to which this entry's addressing information  pertains. The address type of this object is specified in  ipAddressAddrType.  Implementors need to be aware that if the size of  ipAddressAddr exceeds 116 octets, then OIDS of instances of  columns in this row will have more than 128 sub-identifiers  and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3."
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.3
Name: ipAddressIfIndex(3)
Description: ipAddressIfIndex OBJECT-TYPE  SYNTAX InterfaceIndex  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The index value that uniquely identifies the interface to  which this entry is applicable. The interface identified by  a particular value of this index is the same interface as  identified by the same value of the IF-MIB's ifIndex."
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.4
Name: ipAddressType(4)
Description: ipAddressType OBJECT-TYPE  SYNTAX INTEGER {  unicast(1), anycast(2), broadcast(3) }  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The type of address. broadcast(3) is not a valid value for  IPv6 addresses (RFC 3513)."  DEFVAL { unicast }
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.5
Name: ipAddressPrefix(5)
Description: ipAddressPrefix OBJECT-TYPE  SYNTAX RowPointer  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A pointer to the row in the prefix table to which this  address belongs. May be { 0 0 } if there is no such row."  DEFVAL { zeroDotZero }
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.6
Name: ipAddressOrigin(6)
Description: ipAddressOrigin OBJECT-TYPE  SYNTAX IpAddressOriginTC  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The origin of the address."
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.7
Name: ipAddressStatus(7)
Description: ipAddressStatus OBJECT-TYPE  SYNTAX IpAddressStatusTC  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The status of the address, describing if the address can be  used for communication.  In the absence of other information, an IPv4 address is  always preferred(1)."  DEFVAL { preferred }
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.8
Name: ipAddressCreated(8)
Description: ipAddressCreated OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime at the time this entry was created.  If this entry was created prior to the last re-  initialization of the local network management subsystem,  then this object contains a zero value."
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.9
Name: ipAddressLastChanged(9)
Description: ipAddressLastChanged OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime at the time this entry was last  updated. If this entry was updated prior to the last re-  initialization of the local network management subsystem,  then this object contains a zero value."
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.10
Name: ipAddressRowStatus(10)
Description: ipAddressRowStatus OBJECT-TYPE  SYNTAX RowStatus  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The status of this conceptual row.  The RowStatus TC requires that this DESCRIPTION clause  states under which circumstances other objects in this row  can be modified. The value of this object has no effect on  whether other objects in this conceptual row can be  modified.  A conceptual row can not be made active until the  ipAddressIfIndex has been set to a valid index."
----------------------------------------
OID: 1.3.6.1.2.1.4.34.1.11
Name: ipAddressStorageType(11)
Description: ipAddressStorageType OBJECT-TYPE  SYNTAX StorageType  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The storage type for this conceptual row. If this object  has a value of 'permanent', then no other objects are  required to be able to be modified."  DEFVAL { volatile }
----------------------------------------
OID: 1.3.6.1.2.1.4.35.1.1
Name: N/A
Description: ipNetToPhysicalIfIndex OBJECT-TYPE  SYNTAX InterfaceIndex  MAX-ACCESS not-accessible  STATUS current  DESCRIPTION  "The index value that uniquely identifies the interface to  which this entry is applicable. The interface identified by  a particular value of this index is the same interface as  identified by the same value of the IF-MIB's ifIndex."
----------------------------------------
OID: 1.3.6.1.2.1.4.35.1.2
Name: N/A
Description: ipNetToPhysicalNetAddressType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS not-accessible  STATUS current  DESCRIPTION  "The type of ipNetToPhysicalNetAddress."
----------------------------------------
OID: 1.3.6.1.2.1.4.35.1.3
Name: N/A
Description: ipNetToPhysicalNetAddress OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS not-accessible  STATUS current  DESCRIPTION  "The IP Address corresponding to the media-dependent  `physical' address. The address type of this object is  specified in ipNetToPhysicalAddressType.  Implementors need to be aware that if the size of  ipNetToPhysicalNetAddress exceeds 115 octets, then OIDS of  instances of columns in this row will have more than 128  sub-identifiers and cannot be accessed using SNMPv1,  SNMPv2c, or SNMPv3."
----------------------------------------
OID: 1.3.6.1.2.1.4.35.1.4
Name: N/A
Description: ipNetToPhysicalPhysAddress OBJECT-TYPE  SYNTAX PhysAddress (SIZE(0..65535))  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The media-dependent `physical' address.  As the entries in this table are typically not persistent  when this object is written the entity SHOULD NOT save the  change to non-volatile storage."
----------------------------------------
OID: 1.3.6.1.2.1.4.35.1.5
Name: N/A
Description: ipNetToPhysicalLastUpdated OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime at the time this entry was last  updated. If this entry was updated prior to the last re-  initialization of the local network management subsystem,  then this object contains a zero value."
----------------------------------------
OID: 1.3.6.1.2.1.4.35.1.6
Name: ipNetToPhysicalType(6)
Description: ipNetToPhysicalType OBJECT-TYPE  SYNTAX INTEGER {  other(1), -- none of the following  invalid(2), -- an invalidated mapping  dynamic(3),  static(4),  local(5) -- local interface  }  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The type of mapping.  Setting this object to the value invalid(2) has the effect  of invalidating the corresponding entry in the  ipNetToPhysicalTable. That is, it effectively dis-  associates the interface identified with said entry from the  mapping identified with said entry. It is an  implementation-specific matter as to whether the agent  removes an invalidated entry from the table. Accordingly,  management stations must be prepared to receive tabular  information from agents that corresponds to entries not  currently in use. Proper interpretation of such entries  requires examination of the relevant ipNetToPhysicalType  object.  The 'dynamic(3)' type indicates that the IP address to  physical addresses mapping has been dynamically resolved  using e.g., IPv4 ARP or the IPv6 Neighbor Discovery  protocol.  The 'static(4)' type indicates that the mapping has been  statically configured. Both of these refer to entries that  provide mappings for other entities addresses.  The 'local(5)' type indicates that the mapping is provided  for an entity's own interface address.  As the entries in this table are typically not persistent  when this object is written the entity SHOULD NOT save the  change to non-volatile storage."  DEFVAL { static }
----------------------------------------
OID: 1.3.6.1.2.1.4.35.1.7
Name: ipNetToPhysicalState(7)
Description: ipNetToPhysicalState OBJECT-TYPE  SYNTAX INTEGER {  reachable(1), -- confirmed reachability  stale(2), -- unconfirmed reachability  delay(3), -- waiting for reachability  -- confirmation before entering  -- the probe state  probe(4), -- actively probing  invalid(5), -- an invalidated mapping  unknown(6), -- state can not be determined  -- for some reason.  incomplete(7) -- address resolution is being  -- performed.  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Neighbor Unreachability Detection state for the  interface when the address mapping in this entry is used.  If Neighbor Unreachability Detection is not in use (e.g. for  IPv4), this object is always unknown(6)."  REFERENCE "RFC 2461"
----------------------------------------
OID: 1.3.6.1.2.1.4.35.1.8
Name: N/A
Description: ipNetToPhysicalRowStatus OBJECT-TYPE  SYNTAX RowStatus  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The status of this conceptual row.  The RowStatus TC requires that this DESCRIPTION clause  states under which circumstances other objects in this row  can be modified. The value of this object has no effect on  whether other objects in this conceptual row can be  modified.  A conceptual row can not be made active until the  ipNetToPhysicalPhysAddress object has been set.  Note that if the ipNetToPhysicalType is set to 'invalid',  the managed node may delete the entry independent of the  state of this object."
----------------------------------------
OID: 1.3.6.1.2.1.11.1
Name: snmpInPkts(1)
Description: snmpInPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of messages delivered to the SNMP entity from the transport service."
----------------------------------------
OID: 1.3.6.1.2.1.11.2
Name: snmpOutPkts(2)
Description: snmpOutPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Messages which were  passed from the SNMP protocol entity to the  transport service."
----------------------------------------
OID: 1.3.6.1.2.1.11.3
Name: snmpInBadVersions(3)
Description: snmpInBadVersions OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of SNMP messages which were delivered  to the SNMP entity and were for an unsupported SNMP  version."
----------------------------------------
OID: 1.3.6.1.2.1.11.4
Name: N/A
Description: snmpInBadCommunityNames OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of community-based SNMP messages (for  example, SNMPv1) delivered to the SNMP entity which  used an SNMP community name not known to said entity.  Also, implementations which authenticate community-based  SNMP messages using check(s) in addition to matching  the community name (for example, by also checking  whether the message originated from a transport address  allowed to use a specified community name) MAY include  in this value the number of messages which failed the  additional check(s). It is strongly RECOMMENDED that  the documentation for any security model which is used  to authenticate community-based SNMP messages specify  the precise conditions that contribute to this value."
----------------------------------------
OID: 1.3.6.1.2.1.11.5
Name: N/A
Description: snmpInBadCommunityUses OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of community-based SNMP messages (for  example, SNMPv1) delivered to the SNMP entity which  represented an SNMP operation that was not allowed for  the SNMP community named in the message. The precise  conditions under which this counter is incremented  (if at all) depend on how the SNMP entity implements  its access control mechanism and how its applications  interact with that access control mechanism. It is  strongly RECOMMENDED that the documentation for any  access control mechanism which is used to control access  to and visibility of MIB instrumentation specify the  precise conditions that contribute to this value."
----------------------------------------
OID: 1.3.6.1.2.1.11.6
Name: snmpInASNParseErrs(6)
Description: snmpInASNParseErrs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of ASN.1 or BER errors encountered by  the SNMP entity when decoding received SNMP messages."
----------------------------------------
OID: 1.3.6.1.2.1.11.8
Name: snmpInTooBigs(8)
Description: snmpInTooBigs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were  delivered to the SNMP protocol entity and for  which the value of the error-status field was  `tooBig'."
----------------------------------------
OID: 1.3.6.1.2.1.11.9
Name: snmpInNoSuchNames(9)
Description: snmpInNoSuchNames OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were  delivered to the SNMP protocol entity and for  which the value of the error-status field was  `noSuchName'."
----------------------------------------
OID: 1.3.6.1.2.1.11.10
Name: snmpInBadValues(10)
Description: snmpInBadValues OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were  delivered to the SNMP protocol entity and for  which the value of the error-status field was  `badValue'."
----------------------------------------
OID: 1.3.6.1.2.1.11.11
Name: snmpInReadOnlys(11)
Description: snmpInReadOnlys OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number valid SNMP PDUs which were delivered  to the SNMP protocol entity and for which the value  of the error-status field was `readOnly'. It should  be noted that it is a protocol error to generate an  SNMP PDU which contains the value `readOnly' in the  error-status field, as such this object is provided  as a means of detecting incorrect implementations of  the SNMP."
----------------------------------------
OID: 1.3.6.1.2.1.11.12
Name: snmpInGenErrs(12)
Description: snmpInGenErrs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were delivered  to the SNMP protocol entity and for which the value  of the error-status field was `genErr'."
----------------------------------------
OID: 1.3.6.1.2.1.11.13
Name: snmpInTotalReqVars(13)
Description: snmpInTotalReqVars OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of MIB objects which have been  retrieved successfully by the SNMP protocol entity  as the result of receiving valid SNMP Get-Request  and Get-Next PDUs."
----------------------------------------
OID: 1.3.6.1.2.1.11.14
Name: snmpInTotalSetVars(14)
Description: snmpInTotalSetVars OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of MIB objects which have been  altered successfully by the SNMP protocol entity as  the result of receiving valid SNMP Set-Request PDUs."
----------------------------------------
OID: 1.3.6.1.2.1.11.15
Name: snmpInGetRequests(15)
Description: snmpInGetRequests OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Request PDUs which  have been accepted and processed by the SNMP  protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.16
Name: snmpInGetNexts(16)
Description: snmpInGetNexts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Next PDUs which have been  accepted and processed by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.17
Name: snmpInSetRequests(17)
Description: snmpInSetRequests OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Set-Request PDUs which  have been accepted and processed by the SNMP protocol  entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.18
Name: snmpInGetResponses(18)
Description: snmpInGetResponses OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Response PDUs which  have been accepted and processed by the SNMP protocol  entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.19
Name: snmpInTraps(19)
Description: snmpInTraps OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Trap PDUs which have been  accepted and processed by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.20
Name: snmpOutTooBigs(20)
Description: snmpOutTooBigs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were generated  by the SNMP protocol entity and for which the value  of the error-status field was `tooBig.'"
----------------------------------------
OID: 1.3.6.1.2.1.11.21
Name: snmpOutNoSuchNames(21)
Description: snmpOutNoSuchNames OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were generated  by the SNMP protocol entity and for which the value  of the error-status was `noSuchName'."
----------------------------------------
OID: 1.3.6.1.2.1.11.22
Name: snmpOutBadValues(22)
Description: snmpOutBadValues OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were generated  by the SNMP protocol entity and for which the value  of the error-status field was `badValue'."
----------------------------------------
OID: 1.3.6.1.2.1.11.24
Name: snmpOutGenErrs(24)
Description: snmpOutGenErrs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were generated  by the SNMP protocol entity and for which the value  of the error-status field was `genErr'."
----------------------------------------
OID: 1.3.6.1.2.1.11.25
Name: snmpOutGetRequests(25)
Description: snmpOutGetRequests OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Request PDUs which  have been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.26
Name: snmpOutGetNexts(26)
Description: snmpOutGetNexts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Next PDUs which have  been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.27
Name: snmpOutSetRequests(27)
Description: snmpOutSetRequests OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Set-Request PDUs which  have been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.28
Name: snmpOutGetResponses(28)
Description: snmpOutGetResponses OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Response PDUs which  have been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.29
Name: snmpOutTraps(29)
Description: snmpOutTraps OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Trap PDUs which have  been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.30
Name: N/A
Description: snmpEnableAuthenTraps OBJECT-TYPE  SYNTAX INTEGER {enabled(1), disabled(2)}  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "Indicates whether the SNMP entity is permitted to generate authenticationFailure traps. The value of this object overrides any configuration information; as such, it provides a means whereby all authenticationFailure traps may be disabled.  Note that it is strongly recommended that this object be stored in non-volatile memory so that it remains constant across re-initializations of the network management system."
----------------------------------------
OID: 1.3.6.1.2.1.11.31
Name: snmpSilentDrops(31)
Description: snmpSilentDrops OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of Confirmed Class PDUs (such as  GetRequest-PDUs, GetNextRequest-PDUs,  GetBulkRequest-PDUs, SetRequest-PDUs, and  InformRequest-PDUs) delivered to the SNMP entity which  were silently dropped because the size of a reply  containing an alternate Response Class PDU (such as a  Response-PDU) with an empty variable-bindings field  was greater than either a local constraint or the  maximum message size associated with the originator of  the request."
----------------------------------------
OID: 1.3.6.1.2.1.11.32
Name: snmpProxyDrops(32)
Description: snmpProxyDrops OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of Confirmed Class PDUs  (such as GetRequest-PDUs, GetNextRequest-PDUs,  GetBulkRequest-PDUs, SetRequest-PDUs, and  InformRequest-PDUs) delivered to the SNMP entity which  were silently dropped because the transmission of  the (possibly translated) message to a proxy target  failed in a manner (other than a time-out) such that  no Response Class PDU (such as a Response-PDU) could  be returned."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.1
Name: ifName(1)
Description: ifName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The textual name of the interface. The value of this  object should be the name of the interface as assigned by  the local device and should be suitable for use in commands  entered at the device's `console'. This might be a text  name, such as `le0' or a simple port number, such as `1',  depending on the interface naming syntax of the device. If  several entries in the ifTable together represent a single  interface as named by the device, then each will have the  same value of ifName. Note that for an agent which responds  to SNMP queries concerning an interface on some other  (proxied) device, then the value of ifName for such an  interface is the proxied device's local name for it.  If there is no local name, or this object is otherwise not  applicable, then this object contains a zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.2
Name: ifInMulticastPkts(2)
Description: ifInMulticastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a multicast  address at this sub-layer. For a MAC layer protocol, this  includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.3
Name: ifInBroadcastPkts(3)
Description: ifInBroadcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a broadcast  address at this sub-layer.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.4
Name: ifOutMulticastPkts(4)
Description: ifOutMulticastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  multicast address at this sub-layer, including those that  were discarded or not sent. For a MAC layer protocol, this  includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.5
Name: ifOutBroadcastPkts(5)
Description: ifOutBroadcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  broadcast address at this sub-layer, including those that  were discarded or not sent.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.6
Name: ifHCInOctets(6)
Description: ifHCInOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received on the interface,  including framing characters. This object is a 64-bit  version of ifInOctets.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.7
Name: ifHCInUcastPkts(7)
Description: ifHCInUcastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were not addressed to a multicast  or broadcast address at this sub-layer. This object is a  64-bit version of ifInUcastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.8
Name: ifHCInMulticastPkts(8)
Description: ifHCInMulticastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a multicast  address at this sub-layer. For a MAC layer protocol, this  includes both Group and Functional addresses. This object  is a 64-bit version of ifInMulticastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.9
Name: ifHCInBroadcastPkts(9)
Description: ifHCInBroadcastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a broadcast  address at this sub-layer. This object is a 64-bit version  of ifInBroadcastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.10
Name: ifHCOutOctets(10)
Description: ifHCOutOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets transmitted out of the  interface, including framing characters. This object is a  64-bit version of ifOutOctets.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.11
Name: ifHCOutUcastPkts(11)
Description: ifHCOutUcastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were not addressed to a  multicast or broadcast address at this sub-layer, including  those that were discarded or not sent. This object is a  64-bit version of ifOutUcastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.12
Name: ifHCOutMulticastPkts(12)
Description: ifHCOutMulticastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  multicast address at this sub-layer, including those that  were discarded or not sent. For a MAC layer protocol, this  includes both Group and Functional addresses. This object  is a 64-bit version of ifOutMulticastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.13
Name: ifHCOutBroadcastPkts(13)
Description: ifHCOutBroadcastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  broadcast address at this sub-layer, including those that  were discarded or not sent. This object is a 64-bit version  of ifOutBroadcastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.14
Name: N/A
Description: ifLinkUpDownTrapEnable OBJECT-TYPE  SYNTAX INTEGER { enabled(1), disabled(2) }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "Indicates whether linkUp/linkDown traps should be generated  for this interface.  By default, this object should have the value enabled(1) for  interfaces which do not operate on 'top' of any other  interface (as defined in the ifStackTable), and disabled(2)  otherwise."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.15
Name: ifHighSpeed(15)
Description: ifHighSpeed OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An estimate of the interface's current bandwidth in units  of 1,000,000 bits per second. If this object reports a  value of `n' then the speed of the interface is somewhere in  the range of `n-500,000' to `n+499,999'. For interfaces  which do not vary in bandwidth or for those where no  accurate estimation can be made, this object should contain  the nominal bandwidth. For a sub-layer which has no concept  of bandwidth, this object should be zero."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.16
Name: ifPromiscuousMode(16)
Description: ifPromiscuousMode OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object has a value of false(2) if this interface only  accepts packets/frames that are addressed to this station.  This object has a value of true(1) when the station accepts  all packets/frames transmitted on the media. The value  true(1) is only legal on certain types of media. If legal,  setting this object to a value of true(1) may require the  interface to be reset before becoming effective.  The value of ifPromiscuousMode does not affect the reception  of broadcast and multicast packets/frames by the interface."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.17
Name: ifConnectorPresent(17)
Description: ifConnectorPresent OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This object has the value 'true(1)' if the interface  sublayer has a physical connector and the value 'false(2)'  otherwise."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.18
Name: ifAlias(18)
Description: ifAlias OBJECT-TYPE  SYNTAX DisplayString (SIZE(0..64))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object is an 'alias' name for the interface as specified by a network manager, and provides a non-volatile 'handle' for the interface.  On the first instantiation of an interface, the value of ifAlias associated with that interface is the zero-length string. As and when a value is written into an instance of ifAlias through a network management set operation, then the agent must retain the supplied value in the ifAlias instance associated with the same interface for as long as that interface remains instantiated, including across all re-initializations/reboots of the network management system, including those which result in a change of the interface's ifIndex value.  An example of the value which a network manager might store in this object for a WAN interface is the (Telco's) circuit number/identifier of the interface.  Some agents may support write-access only for interfaces having particular values of ifType. An agent which supports write access to this object is required to keep the value in non-volatile storage, but it may limit the length of new values depending on how much storage is already occupied by the current values for other interfaces."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.19
Name: N/A
Description: ifCounterDiscontinuityTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime on the most recent occasion at which  any one or more of this interface's counters suffered a  discontinuity. The relevant counters are the specific  instances associated with this interface of any Counter32 or  Counter64 object contained in the ifTable or ifXTable. If  no such discontinuities have occurred since the last re-  initialization of the local management subsystem, then this  object contains a zero value."
----------------------------------------
OID: 1.3.6.1.2.1.88.1.1.1
Name: N/A
Description: mteResourceSampleMinimum OBJECT-TYPE  SYNTAX Integer32 (1..2147483647)  UNITS "seconds"  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The minimum mteTriggerFrequency this system will  accept. A system may use the larger values of this minimum to  lessen the impact of constant sampling. For larger  sampling intervals the system samples less often and  suffers less overhead. This object provides a way to enforce  such lower overhead for all triggers created after it is  set.  Unless explicitly resource limited, a system's value for  this object SHOULD be 1, allowing as small as a 1 second  interval for ongoing trigger sampling.  Changing this value will not invalidate an existing setting  of mteTriggerFrequency."
----------------------------------------
OID: 1.3.6.1.2.1.88.1.1.2
Name: N/A
Description: mteResourceSampleInstanceMaximum OBJECT-TYPE  SYNTAX Unsigned32  UNITS "instances"  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The maximum number of instance entries this system will  support for sampling.  These are the entries that maintain state, one for each  instance of each sampled object as selected by  mteTriggerValueID. Note that wildcarded objects result  in multiple instances of this state.  A value of 0 indicates no preset limit, that is, the limit  is dynamic based on system operation and resources.  Unless explicitly resource limited, a system's value for  this object SHOULD be 0.  Changing this value will not eliminate or inhibit existing  sample state but could prevent allocation of additional state  information."
----------------------------------------
OID: 1.3.6.1.2.1.88.1.1.3
Name: N/A
Description: mteResourceSampleInstances OBJECT-TYPE  SYNTAX Gauge32  UNITS "instances"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of currently active instance entries as  defined for mteResourceSampleInstanceMaximum."
----------------------------------------
OID: 1.3.6.1.2.1.88.1.1.4
Name: N/A
Description: mteResourceSampleInstancesHigh OBJECT-TYPE  SYNTAX Gauge32  UNITS "instances"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The highest value of mteResourceSampleInstances that has  occurred since initialization of the management system."
----------------------------------------
OID: 1.3.6.1.2.1.88.1.1.5
Name: N/A
Description: mteResourceSampleInstanceLacks OBJECT-TYPE  SYNTAX Counter32  UNITS "instances"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times this system could not take a new sample  because that allocation would have exceeded the limit set by  mteResourceSampleInstanceMaximum."
----------------------------------------
OID: 1.3.6.1.2.1.88.1.2.1
Name: mteTriggerFailures(1)
Description: mteTriggerFailures OBJECT-TYPE  SYNTAX Counter32  UNITS "failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times an attempt to check for a trigger  condition has failed. This counts individually for each  attempt in a group of targets or each attempt for a  wildcarded object."
----------------------------------------
OID: 1.3.6.1.2.1.88.1.4.1
Name: mteEventFailures(1)
Description: mteEventFailures OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times an attempt to invoke an event  has failed. This counts individually for each  attempt in a group of targets or each attempt for a  wildcarded trigger object."
----------------------------------------
OID: 1.3.6.1.2.1.123.1.4.1.2
Name: natAddrMapName(2)
Description: natAddrMapName OBJECT-TYPE  SYNTAX SnmpAdminString (SIZE(1..32))  MAX-ACCESS read-create  STATUS deprecated  DESCRIPTION  "Name identifying all map entries in the table associated  with the same interface. All map entries with the same  ifIndex MUST have the same map name.  Deprecated in favor of NATV2-MIB."  REFERENCE "RFC 7658, RFC 7659"
----------------------------------------
OID: 1.3.6.1.2.1.123.1.4.1.10
Name: N/A
Description: natAddrMapGlobalAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-create  STATUS deprecated  DESCRIPTION  "This object specifies the address type used for  natAddrMapGlobalAddrFrom and natAddrMapGlobalAddrTo.  Deprecated in favor of NATV2-MIB."  REFERENCE "RFC 7658, RFC 7659"
----------------------------------------
OID: 1.3.6.1.2.1.123.1.4.1.11
Name: N/A
Description: natAddrMapGlobalAddrFrom OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-create  STATUS deprecated  DESCRIPTION  "This object specifies the first IP address of the range  of IP addresses being mapped to. The value of this  object must be less than or equal to the value of the  natAddrMapGlobalAddrTo object.  The type of this address is determined by the value of  the natAddrMapGlobalAddrType object.  Deprecated in favor of NATV2-MIB."  REFERENCE "RFC 7658, RFC 7659"
----------------------------------------
OID: 1.3.6.1.2.1.123.1.4.1.12
Name: N/A
Description: natAddrMapGlobalAddrTo OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-create  STATUS deprecated  DESCRIPTION  "This object specifies the last IP address of the range  of IP addresses being mapped to. If only a single  address is being mapped to, the value of this object is  equal to the value of natAddrMapGlobalAddrFrom. For a  static NAT, the number of addresses in the range defined  by natAddrMapGlobalAddrFrom and natAddrMapGlobalAddrTo  must be equal to the number of addresses in the range  defined by natAddrMapLocalAddrFrom and  natAddrMapLocalAddrTo. The value of this object must be  greater than or equal to the value of the  natAddrMapGlobalAddrFrom object.  The type of this address is determined by the value of  the natAddrMapGlobalAddrType object.  Deprecated in favor of NATV2-MIB."  REFERENCE "RFC 7658, RFC 7659"
----------------------------------------
OID: 1.3.6.1.2.1.123.1.4.1.13
Name: N/A
Description: natAddrMapGlobalPortFrom OBJECT-TYPE  SYNTAX InetPortNumber  MAX-ACCESS read-create  STATUS deprecated  DESCRIPTION  "If this conceptual row describes a Basic NAT address  mapping, then the value of this object must be zero. If  this conceptual row describes NAPT, then the value of  this object specifies the first port number in the range  of ports being mapped to.  The value of this object must be less than or equal to  the value of the natAddrMapGlobalPortTo object. If the  translation specifies a single port, then the value of  this object is equal to the value  natAddrMapGlobalPortTo.  Deprecated in favor of NATV2-MIB."  REFERENCE "RFC 7658, RFC 7659"  DEFVAL { 0 }
----------------------------------------
OID: 1.3.6.1.2.1.123.1.4.1.14
Name: N/A
Description: natAddrMapGlobalPortTo OBJECT-TYPE  SYNTAX InetPortNumber  MAX-ACCESS read-create  STATUS deprecated  DESCRIPTION  "If this conceptual row describes a Basic NAT address  mapping, then the value of this object must be zero. If  this conceptual row describes NAPT, then the value of  this object specifies the last port number in the range  of ports being mapped to.  The value of this object must be greater than or equal  to the value of the natAddrMapGlobalPortFrom object. If  the translation specifies a single port, then the value  of this object is equal to the value of  natAddrMapGlobalPortFrom.  Deprecated in favor of NATV2-MIB."  REFERENCE "RFC 7658, RFC 7659"  DEFVAL { 0 }
----------------------------------------
OID: 1.3.6.1.2.1.123.1.4.1.15
Name: natAddrMapProtocol(15)
Description: natAddrMapProtocol OBJECT-TYPE  SYNTAX NatProtocolMap  MAX-ACCESS read-create  STATUS deprecated  DESCRIPTION  "This object specifies a bitmap of protocol identifiers.  Deprecated in favor of NATV2-MIB."  REFERENCE "RFC 7658, RFC 7659"
----------------------------------------
OID: 1.3.6.1.2.1.123.1.4.1.19
Name: natAddrMapAddrUsed(19)
Description: natAddrMapAddrUsed OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The number of addresses pertaining to this address map  that are currently being used from the NAT pool.  The value of this object must always be zero in the case  of a static address map.  Deprecated in favor of NATV2-MIB."  REFERENCE "RFC 7658, RFC 7659"
----------------------------------------
OID: 1.3.6.1.2.1.1.1.
Name: sysDescr(1)
Description: sysDescr OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A textual description of the entity. This value should  include the full name and version identification of  the system's hardware type, software operating-system,  and networking software."
----------------------------------------
OID: 1.3.6.1.2.1.1.2.
Name: sysObjectID(2)
Description: sysObjectID OBJECT-TYPE  SYNTAX OBJECT IDENTIFIER  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The vendor's authoritative identification of the  network management subsystem contained in the entity.  This value is allocated within the SMI enterprises  subtree (1.3.6.1.4.1) and provides an easy and  unambiguous means for determining `what kind of box' is  being managed. For example, if vendor `Flintstones,  Inc.' was assigned the subtree 1.3.6.1.4.1.424242,  it could assign the identifier 1.3.6.1.4.1.424242.1.1  to its `Fred Router'."
----------------------------------------
OID: 1.3.6.1.2.1.1.3.
Name: sysUpTime(3)
Description: sysUpTime OBJECT-TYPE  SYNTAX TimeTicks  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The time (in hundredths of a second) since the  network management portion of the system was last  re-initialized."
----------------------------------------
OID: 1.3.6.1.2.1.1.4.
Name: sysContact(4)
Description: sysContact OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The textual identification of the contact person for  this managed node, together with information on how  to contact this person. If no contact information is  known, the value is the zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.1.5.
Name: sysName(5)
Description: sysName OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "An administratively-assigned name for this managed  node. By convention, this is the node's fully-qualified  domain name. If the name is unknown, the value is  the zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.1.6.
Name: sysLocation(6)
Description: sysLocation OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The physical location of this node (e.g., 'telephone  closet, 3rd floor'). If the location is unknown, the  value is the zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.1.7.
Name: sysServices(7)
Description: sysServices OBJECT-TYPE  SYNTAX INTEGER (0..127)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A value which indicates the set of services that this  entity may potentially offer. The value is a sum.  This sum initially takes the value zero. Then, for  each layer, L, in the range 1 through 7, that this node  performs transactions for, 2 raised to (L - 1) is added  to the sum. For example, a node which performs only  routing functions would have a value of 4 (2^(3-1)).  In contrast, a node which is a host offering application  services would have a value of 72 (2^(4-1) + 2^(7-1)).  Note that in the context of the Internet suite of  protocols, values should be calculated accordingly:  layer functionality  1 physical (e.g., repeaters)  2 datalink/subnetwork (e.g., bridges)  3 internet (e.g., supports the IP)  4 end-to-end (e.g., supports the TCP)  7 applications (e.g., supports the SMTP)  For systems including OSI protocols, layers 5 and 6  may also be counted."
----------------------------------------
OID: 1.3.6.1.2.1.2.1.
Name: ifNumber(1)
Description: ifNumber OBJECT-TYPE  SYNTAX INTEGER  ACCESS read-only  STATUS mandatory  DESCRIPTION  "The number of network interfaces (regardless of their current state) present on this system."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.1.
Name: ifIndex(1)
Description: ifIndex OBJECT-TYPE  SYNTAX InterfaceIndex  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A unique value, greater than zero, for each interface. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub-layer must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.2.
Name: ifDescr(2)
Description: ifDescr OBJECT-TYPE  SYNTAX DisplayString (SIZE (0..255))  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A textual string containing information about theinterface. This string should include the name of the manufacturer, the product name and the version of the interface hardware/software."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.3.
Name: ifType(3)
Description: N/A
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.4.
Name: ifMtu(4)
Description: ifMtu OBJECT-TYPE  SYNTAX Integer32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The size of the largest packet which can be sent/received on the interface, specified in octets. For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.5.
Name: ifSpeed(5)
Description: ifSpeed OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An estimate of the interface's current bandwidth in bits  per second. For interfaces which do not vary in bandwidth  or for those where no accurate estimation can be made, this  object should contain the nominal bandwidth. If the  bandwidth of the interface is greater than the maximum value  reportable by this object then this object should report its  maximum value (4,294,967,295) and ifHighSpeed must be used  to report the interace's speed. For a sub-layer which has  no concept of bandwidth, this object should be zero."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.6.
Name: ifPhysAddress(6)
Description: ifPhysAddress OBJECT-TYPE  SYNTAX PhysAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The interface's address at its protocol sub-layer. For  example, for an 802.x interface, this object normally  contains a MAC address. The interface's media-specific MIB  must define the bit and byte ordering and the format of the  value of this object. For interfaces which do not have such  an address (e.g., a serial line), this object should contain  an octet string of zero length."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.7.
Name: ifAdminStatus(7)
Description: ifAdminStatus OBJECT-TYPE  SYNTAX INTEGER {  up(1), -- ready to pass packets  down(2),  testing(3) -- in some test mode  }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The desired state of the interface. The testing(3) state  indicates that no operational packets can be passed. When a  managed system initializes, all interfaces start with  ifAdminStatus in the down(2) state. As a result of either  explicit management action or per configuration information  retained by the managed system, ifAdminStatus is then  changed to either the up(1) or testing(3) states (or remains  in the down(2) state)."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.8.
Name: ifOperStatus(8)
Description: ifOperStatus OBJECT-TYPE  SYNTAX INTEGER {  up(1), -- ready to pass packets  down(2),  testing(3), -- in some test mode  unknown(4), -- status can not be determined  -- for some reason.  dormant(5),  notPresent(6), -- some component is missing  lowerLayerDown(7) -- down due to state of  -- lower-layer interface(s)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The current operational state of the interface. The  testing(3) state indicates that no operational packets can  be passed. If ifAdminStatus is down(2) then ifOperStatus  should be down(2). If ifAdminStatus is changed to up(1)  then ifOperStatus should change to up(1) if the interface is  ready to transmit and receive network traffic; it should  change to dormant(5) if the interface is waiting for  external actions (such as a serial line waiting for an  incoming connection); it should remain in the down(2) state  if and only if there is a fault that prevents it from going  to the up(1) state; it should remain in the notPresent(6)  state if the interface has missing (typically, hardware)  components."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.9.
Name: ifLastChange(9)
Description: ifLastChange OBJECT-TYPE  SYNTAX TimeTicks  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime at the time the interface entered  its current operational state. If the current state was  entered prior to the last re-initialization of the local  network management subsystem, then this object contains a  zero value."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.10.
Name: ifInOctets(10)
Description: ifInOctets OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received on the interface,  including framing characters.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.11.
Name: ifInUcastPkts(11)
Description: ifInUcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were not addressed to a multicast  or broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.12.
Name: ifInNUcastPkts(12)
Description: ifInNUcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a multicast or  broadcast address at this sub-layer.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime.  This object is deprecated in favour of ifInMulticastPkts and  ifInBroadcastPkts."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.13.
Name: ifInDiscards(13)
Description: ifInDiscards OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of inbound packets which were chosen to be  discarded even though no errors had been detected to prevent  their being deliverable to a higher-layer protocol. One  possible reason for discarding such a packet could be to  free up buffer space.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.14.
Name: ifInErrors(14)
Description: ifInErrors OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "For packet-oriented interfaces, the number of inbound  packets that contained errors preventing them from being  deliverable to a higher-layer protocol. For character-  oriented or fixed-length interfaces, the number of inbound  transmission units that contained errors preventing them  from being deliverable to a higher-layer protocol.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.16.
Name: ifOutOctets(16)
Description: ifOutOctets OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets transmitted out of the  interface, including framing characters.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.17.
Name: ifOutUcastPkts(17)
Description: ifOutUcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were not addressed to a  multicast or broadcast address at this sub-layer, including  those that were discarded or not sent.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.18.
Name: ifOutNUcastPkts(18)
Description: ifOutNUcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  multicast or broadcast address at this sub-layer, including  those that were discarded or not sent.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime.  This object is deprecated in favour of ifOutMulticastPkts  and ifOutBroadcastPkts."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.19.
Name: ifOutDiscards(19)
Description: ifOutDiscards OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of outbound packets which were chosen to be  discarded even though no errors had been detected to prevent  their being transmitted. One possible reason for discarding  such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.20.
Name: ifOutErrors(20)
Description: ifOutErrors OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "For packet-oriented interfaces, the number of outbound  packets that could not be transmitted because of errors.  For character-oriented or fixed-length interfaces, the  number of outbound transmission units that could not be  transmitted because of errors.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.21.
Name: ifOutQLen(21)
Description: ifOutQLen OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The length of the output packet queue (in packets)."
----------------------------------------
OID: 1.3.6.1.2.1.2.2.1.22.
Name: ifSpecific(22)
Description: ifSpecific OBJECT-TYPE  SYNTAX OBJECT IDENTIFIER  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "A reference to MIB definitions specific to the particular  media being used to realize the interface. It is  recommended that this value point to an instance of a MIB  object in the media-specific MIB, i.e., that this object  have the semantics associated with the InstancePointer  textual convention defined in RFC 2579. In fact, it is  recommended that the media-specific MIB specify what value  ifSpecific should/can take for values of ifType. If no MIB  definitions specific to the particular media are available,  the value should be set to the OBJECT IDENTIFIER { 0 0 }."
----------------------------------------
OID: 1.3.6.1.2.1.4.1.
Name: ipForwarding(1)
Description: ipForwarding OBJECT-TYPE  SYNTAX INTEGER {  forwarding(1), -- acting as a router  notForwarding(2) -- NOT acting as a router  }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The indication of whether this entity is acting as an IPv4  router in respect to the forwarding of datagrams received  by, but not addressed to, this entity. IPv4 routers forward  datagrams. IPv4 hosts do not (except those source-routed  via the host).  When this object is written, the entity should save the  change to non-volatile storage and restore the object from  non-volatile storage upon re-initialization of the system.  Note: a stronger requirement is not used because this object  was previously defined."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.1.
Name: ipAdEntAddr(1)
Description: ipAdEntAddr OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The IPv4 address to which this entry's addressing  information pertains."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.2.
Name: ipAdEntIfIndex(2)
Description: ipAdEntIfIndex OBJECT-TYPE  SYNTAX INTEGER (1..2147483647)  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The index value which uniquely identifies the interface to  which this entry is applicable. The interface identified by  a particular value of this index is the same interface as  identified by the same value of the IF-MIB's ifIndex."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.3.
Name: ipAdEntNetMask(3)
Description: ipAdEntNetMask OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The subnet mask associated with the IPv4 address of this  entry. The value of the mask is an IPv4 address with all  the network bits set to 1 and all the hosts bits set to 0."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.4.
Name: ipAdEntBcastAddr(4)
Description: ipAdEntBcastAddr OBJECT-TYPE  SYNTAX INTEGER (0..1)  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The value of the least-significant bit in the IPv4 broadcast  address used for sending datagrams on the (logical)  interface associated with the IPv4 address of this entry.  For example, when the Internet standard all-ones broadcast  address is used, the value will be 1. This value applies to  both the subnet and network broadcast addresses used by the  entity on this (logical) interface."
----------------------------------------
OID: 1.3.6.1.2.1.4.20.1.5.
Name: ipAdEntReasmMaxSize(5)
Description: ipAdEntReasmMaxSize OBJECT-TYPE  SYNTAX INTEGER (0..65535)  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "The size of the largest IPv4 datagram which this entity can  re-assemble from incoming IPv4 fragmented datagrams received  on this interface."
----------------------------------------
OID: 1.3.6.1.2.1.11.1.
Name: snmpInPkts(1)
Description: snmpInPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of messages delivered to the SNMP entity from the transport service."
----------------------------------------
OID: 1.3.6.1.2.1.11.2.
Name: snmpOutPkts(2)
Description: snmpOutPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Messages which were  passed from the SNMP protocol entity to the  transport service."
----------------------------------------
OID: 1.3.6.1.2.1.11.3.
Name: snmpInBadVersions(3)
Description: snmpInBadVersions OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of SNMP messages which were delivered  to the SNMP entity and were for an unsupported SNMP  version."
----------------------------------------
OID: 1.3.6.1.2.1.11.4.
Name: N/A
Description: snmpInBadCommunityNames OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of community-based SNMP messages (for  example, SNMPv1) delivered to the SNMP entity which  used an SNMP community name not known to said entity.  Also, implementations which authenticate community-based  SNMP messages using check(s) in addition to matching  the community name (for example, by also checking  whether the message originated from a transport address  allowed to use a specified community name) MAY include  in this value the number of messages which failed the  additional check(s). It is strongly RECOMMENDED that  the documentation for any security model which is used  to authenticate community-based SNMP messages specify  the precise conditions that contribute to this value."
----------------------------------------
OID: 1.3.6.1.2.1.11.5.
Name: N/A
Description: snmpInBadCommunityUses OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of community-based SNMP messages (for  example, SNMPv1) delivered to the SNMP entity which  represented an SNMP operation that was not allowed for  the SNMP community named in the message. The precise  conditions under which this counter is incremented  (if at all) depend on how the SNMP entity implements  its access control mechanism and how its applications  interact with that access control mechanism. It is  strongly RECOMMENDED that the documentation for any  access control mechanism which is used to control access  to and visibility of MIB instrumentation specify the  precise conditions that contribute to this value."
----------------------------------------
OID: 1.3.6.1.2.1.11.6.
Name: snmpInASNParseErrs(6)
Description: snmpInASNParseErrs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of ASN.1 or BER errors encountered by  the SNMP entity when decoding received SNMP messages."
----------------------------------------
OID: 1.3.6.1.2.1.11.8.
Name: snmpInTooBigs(8)
Description: snmpInTooBigs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were  delivered to the SNMP protocol entity and for  which the value of the error-status field was  `tooBig'."
----------------------------------------
OID: 1.3.6.1.2.1.11.9.
Name: snmpInNoSuchNames(9)
Description: snmpInNoSuchNames OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were  delivered to the SNMP protocol entity and for  which the value of the error-status field was  `noSuchName'."
----------------------------------------
OID: 1.3.6.1.2.1.11.10.
Name: snmpInBadValues(10)
Description: snmpInBadValues OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were  delivered to the SNMP protocol entity and for  which the value of the error-status field was  `badValue'."
----------------------------------------
OID: 1.3.6.1.2.1.11.11.
Name: snmpInReadOnlys(11)
Description: snmpInReadOnlys OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number valid SNMP PDUs which were delivered  to the SNMP protocol entity and for which the value  of the error-status field was `readOnly'. It should  be noted that it is a protocol error to generate an  SNMP PDU which contains the value `readOnly' in the  error-status field, as such this object is provided  as a means of detecting incorrect implementations of  the SNMP."
----------------------------------------
OID: 1.3.6.1.2.1.11.12.
Name: snmpInGenErrs(12)
Description: snmpInGenErrs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were delivered  to the SNMP protocol entity and for which the value  of the error-status field was `genErr'."
----------------------------------------
OID: 1.3.6.1.2.1.11.13.
Name: snmpInTotalReqVars(13)
Description: snmpInTotalReqVars OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of MIB objects which have been  retrieved successfully by the SNMP protocol entity  as the result of receiving valid SNMP Get-Request  and Get-Next PDUs."
----------------------------------------
OID: 1.3.6.1.2.1.11.14.
Name: snmpInTotalSetVars(14)
Description: snmpInTotalSetVars OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of MIB objects which have been  altered successfully by the SNMP protocol entity as  the result of receiving valid SNMP Set-Request PDUs."
----------------------------------------
OID: 1.3.6.1.2.1.11.15.
Name: snmpInGetRequests(15)
Description: snmpInGetRequests OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Request PDUs which  have been accepted and processed by the SNMP  protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.16.
Name: snmpInGetNexts(16)
Description: snmpInGetNexts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Next PDUs which have been  accepted and processed by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.17.
Name: snmpInSetRequests(17)
Description: snmpInSetRequests OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Set-Request PDUs which  have been accepted and processed by the SNMP protocol  entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.18.
Name: snmpInGetResponses(18)
Description: snmpInGetResponses OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Response PDUs which  have been accepted and processed by the SNMP protocol  entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.19.
Name: snmpInTraps(19)
Description: snmpInTraps OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Trap PDUs which have been  accepted and processed by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.20.
Name: snmpOutTooBigs(20)
Description: snmpOutTooBigs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were generated  by the SNMP protocol entity and for which the value  of the error-status field was `tooBig.'"
----------------------------------------
OID: 1.3.6.1.2.1.11.21.
Name: snmpOutNoSuchNames(21)
Description: snmpOutNoSuchNames OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were generated  by the SNMP protocol entity and for which the value  of the error-status was `noSuchName'."
----------------------------------------
OID: 1.3.6.1.2.1.11.22.
Name: snmpOutBadValues(22)
Description: snmpOutBadValues OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were generated  by the SNMP protocol entity and for which the value  of the error-status field was `badValue'."
----------------------------------------
OID: 1.3.6.1.2.1.11.24.
Name: snmpOutGenErrs(24)
Description: snmpOutGenErrs OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP PDUs which were generated  by the SNMP protocol entity and for which the value  of the error-status field was `genErr'."
----------------------------------------
OID: 1.3.6.1.2.1.11.25.
Name: snmpOutGetRequests(25)
Description: snmpOutGetRequests OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Request PDUs which  have been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.26.
Name: snmpOutGetNexts(26)
Description: snmpOutGetNexts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Next PDUs which have  been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.27.
Name: snmpOutSetRequests(27)
Description: snmpOutSetRequests OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Set-Request PDUs which  have been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.28.
Name: snmpOutGetResponses(28)
Description: snmpOutGetResponses OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Get-Response PDUs which  have been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.29.
Name: snmpOutTraps(29)
Description: snmpOutTraps OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS obsolete  DESCRIPTION  "The total number of SNMP Trap PDUs which have  been generated by the SNMP protocol entity."
----------------------------------------
OID: 1.3.6.1.2.1.11.30.
Name: N/A
Description: snmpEnableAuthenTraps OBJECT-TYPE  SYNTAX INTEGER {enabled(1), disabled(2)}  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "Indicates whether the SNMP entity is permitted to generate authenticationFailure traps. The value of this object overrides any configuration information; as such, it provides a means whereby all authenticationFailure traps may be disabled.  Note that it is strongly recommended that this object be stored in non-volatile memory so that it remains constant across re-initializations of the network management system."
----------------------------------------
OID: 1.3.6.1.2.1.11.31.
Name: snmpSilentDrops(31)
Description: snmpSilentDrops OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of Confirmed Class PDUs (such as  GetRequest-PDUs, GetNextRequest-PDUs,  GetBulkRequest-PDUs, SetRequest-PDUs, and  InformRequest-PDUs) delivered to the SNMP entity which  were silently dropped because the size of a reply  containing an alternate Response Class PDU (such as a  Response-PDU) with an empty variable-bindings field  was greater than either a local constraint or the  maximum message size associated with the originator of  the request."
----------------------------------------
OID: 1.3.6.1.2.1.11.32.
Name: snmpProxyDrops(32)
Description: snmpProxyDrops OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of Confirmed Class PDUs  (such as GetRequest-PDUs, GetNextRequest-PDUs,  GetBulkRequest-PDUs, SetRequest-PDUs, and  InformRequest-PDUs) delivered to the SNMP entity which  were silently dropped because the transmission of  the (possibly translated) message to a proxy target  failed in a manner (other than a time-out) such that  no Response Class PDU (such as a Response-PDU) could  be returned."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.1.
Name: ifName(1)
Description: ifName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The textual name of the interface. The value of this  object should be the name of the interface as assigned by  the local device and should be suitable for use in commands  entered at the device's `console'. This might be a text  name, such as `le0' or a simple port number, such as `1',  depending on the interface naming syntax of the device. If  several entries in the ifTable together represent a single  interface as named by the device, then each will have the  same value of ifName. Note that for an agent which responds  to SNMP queries concerning an interface on some other  (proxied) device, then the value of ifName for such an  interface is the proxied device's local name for it.  If there is no local name, or this object is otherwise not  applicable, then this object contains a zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.2.
Name: ifInMulticastPkts(2)
Description: ifInMulticastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a multicast  address at this sub-layer. For a MAC layer protocol, this  includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.3.
Name: ifInBroadcastPkts(3)
Description: ifInBroadcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a broadcast  address at this sub-layer.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.4.
Name: ifOutMulticastPkts(4)
Description: ifOutMulticastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  multicast address at this sub-layer, including those that  were discarded or not sent. For a MAC layer protocol, this  includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.5.
Name: ifOutBroadcastPkts(5)
Description: ifOutBroadcastPkts OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  broadcast address at this sub-layer, including those that  were discarded or not sent.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.6.
Name: ifHCInOctets(6)
Description: ifHCInOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received on the interface,  including framing characters. This object is a 64-bit  version of ifInOctets.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.7.
Name: ifHCInUcastPkts(7)
Description: ifHCInUcastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were not addressed to a multicast  or broadcast address at this sub-layer. This object is a  64-bit version of ifInUcastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.8.
Name: ifHCInMulticastPkts(8)
Description: ifHCInMulticastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a multicast  address at this sub-layer. For a MAC layer protocol, this  includes both Group and Functional addresses. This object  is a 64-bit version of ifInMulticastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.9.
Name: ifHCInBroadcastPkts(9)
Description: ifHCInBroadcastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets, delivered by this sub-layer to a  higher (sub-)layer, which were addressed to a broadcast  address at this sub-layer. This object is a 64-bit version  of ifInBroadcastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.10.
Name: ifHCOutOctets(10)
Description: ifHCOutOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets transmitted out of the  interface, including framing characters. This object is a  64-bit version of ifOutOctets.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.11.
Name: ifHCOutUcastPkts(11)
Description: ifHCOutUcastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were not addressed to a  multicast or broadcast address at this sub-layer, including  those that were discarded or not sent. This object is a  64-bit version of ifOutUcastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.12.
Name: ifHCOutMulticastPkts(12)
Description: ifHCOutMulticastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  multicast address at this sub-layer, including those that  were discarded or not sent. For a MAC layer protocol, this  includes both Group and Functional addresses. This object  is a 64-bit version of ifOutMulticastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.13.
Name: ifHCOutBroadcastPkts(13)
Description: ifHCOutBroadcastPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets that higher-level protocols  requested be transmitted, and which were addressed to a  broadcast address at this sub-layer, including those that  were discarded or not sent. This object is a 64-bit version  of ifOutBroadcastPkts.  Discontinuities in the value of this counter can occur at  re-initialization of the management system, and at other  times as indicated by the value of  ifCounterDiscontinuityTime."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.14.
Name: N/A
Description: ifLinkUpDownTrapEnable OBJECT-TYPE  SYNTAX INTEGER { enabled(1), disabled(2) }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "Indicates whether linkUp/linkDown traps should be generated  for this interface.  By default, this object should have the value enabled(1) for  interfaces which do not operate on 'top' of any other  interface (as defined in the ifStackTable), and disabled(2)  otherwise."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.15.
Name: ifHighSpeed(15)
Description: ifHighSpeed OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An estimate of the interface's current bandwidth in units  of 1,000,000 bits per second. If this object reports a  value of `n' then the speed of the interface is somewhere in  the range of `n-500,000' to `n+499,999'. For interfaces  which do not vary in bandwidth or for those where no  accurate estimation can be made, this object should contain  the nominal bandwidth. For a sub-layer which has no concept  of bandwidth, this object should be zero."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.16.
Name: ifPromiscuousMode(16)
Description: ifPromiscuousMode OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object has a value of false(2) if this interface only  accepts packets/frames that are addressed to this station.  This object has a value of true(1) when the station accepts  all packets/frames transmitted on the media. The value  true(1) is only legal on certain types of media. If legal,  setting this object to a value of true(1) may require the  interface to be reset before becoming effective.  The value of ifPromiscuousMode does not affect the reception  of broadcast and multicast packets/frames by the interface."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.17.
Name: ifConnectorPresent(17)
Description: ifConnectorPresent OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This object has the value 'true(1)' if the interface  sublayer has a physical connector and the value 'false(2)'  otherwise."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.18.
Name: ifAlias(18)
Description: ifAlias OBJECT-TYPE  SYNTAX DisplayString (SIZE(0..64))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object is an 'alias' name for the interface as specified by a network manager, and provides a non-volatile 'handle' for the interface.  On the first instantiation of an interface, the value of ifAlias associated with that interface is the zero-length string. As and when a value is written into an instance of ifAlias through a network management set operation, then the agent must retain the supplied value in the ifAlias instance associated with the same interface for as long as that interface remains instantiated, including across all re-initializations/reboots of the network management system, including those which result in a change of the interface's ifIndex value.  An example of the value which a network manager might store in this object for a WAN interface is the (Telco's) circuit number/identifier of the interface.  Some agents may support write-access only for interfaces having particular values of ifType. An agent which supports write access to this object is required to keep the value in non-volatile storage, but it may limit the length of new values depending on how much storage is already occupied by the current values for other interfaces."
----------------------------------------
OID: 1.3.6.1.2.1.31.1.1.1.19.
Name: N/A
Description: ifCounterDiscontinuityTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime on the most recent occasion at which  any one or more of this interface's counters suffered a  discontinuity. The relevant counters are the specific  instances associated with this interface of any Counter32 or  Counter64 object contained in the ifTable or ifXTable. If  no such discontinuities have occurred since the last re-  initialization of the local management subsystem, then this  object contains a zero value."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.2.
Name: entPhysicalDescr(2)
Description: entPhysicalDescr OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A textual description of physical entity. This object  should contain a string that identifies the manufacturer's  name for the physical entity and should be set to a  distinct value for each version or model of the physical  entity."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.3.
Name: entPhysicalVendorType(3)
Description: entPhysicalVendorType OBJECT-TYPE  SYNTAX AutonomousType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An indication of the vendor-specific hardware type of the  physical entity. Note that this is different from the  definition of MIB-II's sysObjectID.  An agent should set this object to an enterprise-specific  registration identifier value indicating the specific  equipment type in detail. The associated instance of  entPhysicalClass is used to indicate the general type of  hardware device.  If no vendor-specific registration identifier exists for  this physical entity, or the value is unknown by this agent,  then the value { 0 0 } is returned."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.4.
Name: N/A
Description: entPhysicalContainedIn OBJECT-TYPE  SYNTAX PhysicalIndexOrZero  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of entPhysicalIndex for the physical entity that  'contains' this physical entity. A value of zero indicates  this physical entity is not contained in any other physical  entity. Note that the set of 'containment' relationships  define a strict hierarchy; that is, recursion is not  allowed.  In the event that a physical entity is contained by more  than one physical entity (e.g., double-wide modules), this  object should identify the containing entity with the lowest  value of entPhysicalIndex."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.5.
Name: entPhysicalClass(5)
Description: entPhysicalClass OBJECT-TYPE  SYNTAX IANAPhysicalClass  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An indication of the general hardware type of the physical  entity.  An agent should set this object to the standard enumeration  value that most accurately indicates the general class of  the physical entity, or the primary class if there is more  than one entity.  If no appropriate standard registration identifier exists  for this physical entity, then the value 'other(1)' is  returned. If the value is unknown by this agent, then the  value 'unknown(2)' is returned."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.6.
Name: N/A
Description: entPhysicalParentRelPos OBJECT-TYPE  SYNTAX Integer32 (-1..2147483647)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An indication of the relative position of this 'child'  component among all its 'sibling' components. Sibling  components are defined as entPhysicalEntries that share the  same instance values of each of the entPhysicalContainedIn  and entPhysicalClass objects.  An NMS can use this object to identify the relative ordering  for all sibling components of a particular parent  (identified by the entPhysicalContainedIn instance in each  sibling entry).  If possible, this value should match any external labeling  of the physical component. For example, for a container  (e.g., card slot) labeled as 'slot #3',  entPhysicalParentRelPos should have the value '3'. Note  that the entPhysicalEntry for the module plugged in slot 3  should have an entPhysicalParentRelPos value of '1'.  If the physical position of this component does not match  any external numbering or clearly visible ordering, then  user documentation or other external reference material  should be used to determine the parent-relative position.  If this is not possible, then the agent should assign a  consistent (but possibly arbitrary) ordering to a given set  of 'sibling' components, perhaps based on internal  representation of the components.  If the agent cannot determine the parent-relative position  for some reason, or if the associated value of  entPhysicalContainedIn is '0', then the value '-1' is  returned. Otherwise, a non-negative integer is returned,  indicating the parent-relative position of this physical  entity.  Parent-relative ordering normally starts from '1' and  continues to 'N', where 'N' represents the highest  positioned child entity. However, if the physical entities  (e.g., slots) are labeled from a starting position of zero,  then the first sibling should be associated with an  entPhysicalParentRelPos value of '0'. Note that this  ordering may be sparse or dense, depending on agent  implementation.  The actual values returned are not globally meaningful, as  each 'parent' component may use different numbering  algorithms. The ordering is only meaningful among siblings  of the same parent component.  The agent should retain parent-relative position values  across reboots, either through algorithmic assignment or use  of non-volatile storage."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.7.
Name: entPhysicalName(7)
Description: entPhysicalName OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The textual name of the physical entity. The value of this  object should be the name of the component as assigned by  the local device and should be suitable for use in commands  entered at the device's 'console'. This might be a text  name (e.g., 'console') or a simple component number (e.g.,  port or module number, such as '1'), depending on the  physical component naming syntax of the device.  If there is no local name, or if this object is otherwise  not applicable, then this object contains a zero-length  string.  Note that the value of entPhysicalName for two physical  entities will be the same in the event that the console  interface does not distinguish between them, e.g., slot-1  and the card in slot-1."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.8.
Name: N/A
Description: entPhysicalHardwareRev OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The vendor-specific hardware revision string for the  physical entity. The preferred value is the hardware  revision identifier actually printed on the component itself  (if present).  Note that if revision information is stored internally in a  non-printable (e.g., binary) format, then the agent must  convert such information to a printable format in an  implementation-specific manner.  If no specific hardware revision string is associated with  the physical component, or if this information is unknown to  the agent, then this object will contain a zero-length  string."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.9.
Name: N/A
Description: entPhysicalFirmwareRev OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The vendor-specific firmware revision string for the  physical entity.  Note that if revision information is stored internally in a  non-printable (e.g., binary) format, then the agent must  convert such information to a printable format in an  implementation-specific manner.  If no specific firmware programs are associated with the  physical component, or if this information is unknown to the  agent, then this object will contain a zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.10.
Name: N/A
Description: entPhysicalSoftwareRev OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The vendor-specific software revision string for the  physical entity.  Note that if revision information is stored internally in a  non-printable (e.g., binary) format, then the agent must  convert such information to a printable format in an  implementation-specific manner.  If no specific software programs are associated with the  physical component, or if this information is unknown to the  agent, then this object will contain a zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.11.
Name: entPhysicalSerialNum(11)
Description: entPhysicalSerialNum OBJECT-TYPE  SYNTAX SnmpAdminString (SIZE (0..32))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The vendor-specific serial number string for the physical  entity. The preferred value is the serial number string  actually printed on the component itself (if present).  On the first instantiation of a physical entity, the value  of entPhysicalSerialNum associated with that entity is set  to the correct vendor-assigned serial number, if this  information is available to the agent. If a serial number  is unknown or non-existent, the entPhysicalSerialNum will be  set to a zero-length string instead.  Note that implementations that can correctly identify the  serial numbers of all installed physical entities do not  need to provide write access to the entPhysicalSerialNum  object. Agents that cannot provide non-volatile storage  for the entPhysicalSerialNum strings are not required to  implement write access for this object.  Not every physical component will have a serial number, or  even need one. Physical entities for which the associated  value of the entPhysicalIsFRU object is equal to 'false(2)'  (e.g., the repeater ports within a repeater module) do not  need their own unique serial numbers. An agent does not  have to provide write access for such entities and may  return a zero-length string.  If write access is implemented for an instance of  entPhysicalSerialNum and a value is written into the  instance, the agent must retain the supplied value in the  entPhysicalSerialNum instance (associated with the same  physical entity) for as long as that entity remains  instantiated. This includes instantiations across all  re-initializations/reboots of the network management system,  including those resulting in a change of the physical  entity's entPhysicalIndex value."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.12.
Name: entPhysicalMfgName(12)
Description: entPhysicalMfgName OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The name of the manufacturer of this physical component.  The preferred value is the manufacturer name string actually  printed on the component itself (if present).  Note that comparisons between instances of the  entPhysicalModelName, entPhysicalFirmwareRev,  entPhysicalSoftwareRev, and the entPhysicalSerialNum  objects are only meaningful amongst entPhysicalEntries with  the same value of entPhysicalMfgName.  If the manufacturer name string associated with the physical  component is unknown to the agent, then this object will  contain a zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.13.
Name: entPhysicalModelName(13)
Description: entPhysicalModelName OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The vendor-specific model name identifier string associated with this physical component. The preferred value is the customer-visible part number, which may be printed on the component itself.  If the model name string associated with the physical component is unknown to the agent, then this object will contain a zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.14.
Name: entPhysicalAlias(14)
Description: entPhysicalAlias OBJECT-TYPE  SYNTAX SnmpAdminString (SIZE (0..32))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object is an 'alias' name for the physical entity, as  specified by a network manager, and provides a non-volatile  'handle' for the physical entity.  On the first instantiation of a physical entity, the value  of entPhysicalAlias associated with that entity is set to  the zero-length string. However, the agent may set the  value to a locally unique default value, instead of a  zero-length string.  If write access is implemented for an instance of  entPhysicalAlias and a value is written into the instance,  the agent must retain the supplied value in the  entPhysicalAlias instance (associated with the same physical  entity) for as long as that entity remains instantiated.  This includes instantiations across all  re-initializations/reboots of the network management system,  including those resulting in a change of the physical  entity's entPhysicalIndex value."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.15.
Name: entPhysicalAssetID(15)
Description: entPhysicalAssetID OBJECT-TYPE  SYNTAX SnmpAdminString (SIZE (0..32))  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object is a user-assigned asset tracking identifier  (as specified by a network manager) for the physical entity  and provides non-volatile storage of this information.  On the first instantiation of a physical entity, the value  of entPhysicalAssetID associated with that entity is set to  the zero-length string.  Not every physical component will have an asset tracking  identifier or even need one. Physical entities for which  the associated value of the entPhysicalIsFRU object is equal  to 'false(2)' (e.g., the repeater ports within a repeater  module) do not need their own unique asset tracking  identifier. An agent does not have to provide write access  for such entities and may instead return a zero-length  string.  If write access is implemented for an instance of  entPhysicalAssetID and a value is written into the  instance, the agent must retain the supplied value in the  entPhysicalAssetID instance (associated with the same  physical entity) for as long as that entity remains  instantiated. This includes instantiations across all  re-initializations/reboots of the network management system,  including those resulting in a change of the physical  entity's entPhysicalIndex value.  If no asset tracking information is associated with the  physical component, then this object will contain a  zero-length string."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.1.1.1.16.
Name: entPhysicalIsFRU(16)
Description: entPhysicalIsFRU OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This object indicates whether or not this physical entity  is considered a 'field replaceable unit' by the vendor.  If this object contains the value 'true(1)', then this  entPhysicalEntry identifies a field replaceable unit. For  all entPhysicalEntries that represent components  permanently contained within a field replaceable unit, the  value 'false(2)' should be returned for this object."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.2.1.1.2.
Name: entLogicalDescr(2)
Description: entLogicalDescr OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A textual description of the logical entity. This object  should contain a string that identifies the manufacturer's  name for the logical entity and should be set to a distinct  value for each version of the logical entity."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.2.1.1.3.
Name: entLogicalType(3)
Description: entLogicalType OBJECT-TYPE  SYNTAX AutonomousType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An indication of the type of logical entity. This will  typically be the OBJECT IDENTIFIER name of the node in the  SMI's naming hierarchy that represents the major MIB  module, or the majority of the MIB modules, supported by the  logical entity. For example:  a logical entity of a regular host/router -> mib-2  a logical entity of a 802.1d bridge -> dot1dBridge  a logical entity of a 802.3 repeater -> snmpDot3RptrMgmt  If an appropriate node in the SMI's naming hierarchy cannot  be identified, the value 'mib-2' should be used."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.2.1.1.4.
Name: entLogicalCommunity(4)
Description: entLogicalCommunity OBJECT-TYPE  SYNTAX OCTET STRING (SIZE (0..255))  MAX-ACCESS read-only  STATUS deprecated  DESCRIPTION  "An SNMPv1 or SNMPv2c community string, which can be used to  access detailed management information for this logical  entity. The agent should allow read access with this  community string (to an appropriate subset of all managed  objects) and may also return a community string based on the  privileges of the request used to read this object. Note  that an agent may return a community string with read-only  privileges, even if this object is accessed with a  read-write community string. However, the agent must take  care not to return a community string that allows more  privileges than the community string used to access this  object.  A compliant SNMP agent may wish to conserve naming scopes by  representing multiple logical entities in a single 'default'  naming scope. This is possible when the logical entities,  represented by the same value of entLogicalCommunity, have  no object instances in common. For example, 'bridge1' and  'repeater1' may be part of the main naming scope, but at  least one additional community string is needed to represent  'bridge2' and 'repeater2'.  Logical entities 'bridge1' and 'repeater1' would be  represented by sysOREntries associated with the 'default'  naming scope.  For agents not accessible via SNMPv1 or SNMPv2c, the value  of this object is the empty string. This object may also  contain an empty string if a community string has not yet  been assigned by the agent or if no community string with  suitable access rights can be returned for a particular SNMP  request.  Note that this object is deprecated. Agents that implement  SNMPv3 access should use the entLogicalContextEngineID and  entLogicalContextName objects to identify the context  associated with each logical entity. SNMPv3 agents may  return a zero-length string for this object or may continue  to return a community string (e.g., tri-lingual agent  support)."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.2.1.1.5.
Name: entLogicalTAddress(5)
Description: entLogicalTAddress OBJECT-TYPE  SYNTAX TAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The transport service address by which the logical entity  receives network management traffic, formatted according to  the corresponding value of entLogicalTDomain.  For snmpUDPDomain, a TAddress is 6 octets long: the initial  4 octets contain the IP-address in network-byte order, and  the last 2 contain the UDP port in network-byte order.  Consult RFC 3417 for further information on snmpUDPDomain."  REFERENCE  "Transport Mappings for the Simple Network Management  Protocol (SNMP), STD 62, RFC 3417."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.2.1.1.6.
Name: entLogicalTDomain(6)
Description: entLogicalTDomain OBJECT-TYPE  SYNTAX TDomain  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates the kind of transport service by which the  logical entity receives network management traffic.  Possible values for this object are presently found in  RFC 3417."  REFERENCE  "Transport Mappings for the Simple Network Management  Protocol (SNMP), STD 62, RFC 3417."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.2.1.1.7.
Name: N/A
Description: entLogicalContextEngineID OBJECT-TYPE  SYNTAX SnmpEngineIdOrNone  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authoritative contextEngineID that can be used to send  an SNMP message concerning information held by this logical  entity to the address specified by the associated  'entLogicalTAddress/entLogicalTDomain' pair.  This object, together with the associated  entLogicalContextName object, defines the context associated  with a particular logical entity and allows access to SNMP  engines identified by a contextEngineID and contextName  pair.  If no value has been configured by the agent, a zero-length  string is returned, or the agent may choose not to  instantiate this object at all."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.2.1.1.8.
Name: entLogicalContextName(8)
Description: entLogicalContextName OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The contextName that can be used to send an SNMP message  concerning information held by this logical entity to the  address specified by the associated  'entLogicalTAddress/entLogicalTDomain' pair.  This object, together with the associated  entLogicalContextEngineID object, defines the context  associated with a particular logical entity and allows  access to SNMP engines identified by a contextEngineID and  contextName pair.  If no value has been configured by the agent, a zero-length  string is returned, or the agent may choose not to  instantiate this object at all."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.3.1.1.1.
Name: entLPPhysicalIndex(1)
Description: entLPPhysicalIndex OBJECT-TYPE  SYNTAX PhysicalIndex  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of this object identifies the index value of a  particular entPhysicalEntry associated with the indicated  entLogicalEntity."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.3.2.1.2.
Name: N/A
Description: entAliasMappingIdentifier OBJECT-TYPE  SYNTAX RowPointer  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of this object identifies a particular conceptual  row associated with the indicated entPhysicalIndex and  entLogicalIndex pair.  Because only physical ports are modeled in this table, only  entries that represent interfaces or ports are allowed. If  an ifEntry exists on behalf of a particular physical port,  then this object should identify the associated ifEntry.  For repeater ports, the appropriate row in the  'rptrPortGroupTable' should be identified instead.  For example, suppose a physical port was represented by  entPhysicalEntry.3, entLogicalEntry.15 existed for a  repeater, and entLogicalEntry.22 existed for a bridge. Then  there might be two related instances of  entAliasMappingIdentifier:  entAliasMappingIdentifier.3.15 == rptrPortGroupIndex.5.2  entAliasMappingIdentifier.3.22 == ifIndex.17  It is possible that other mappings (besides interfaces and  repeater ports) may be defined in the future, as required.  Bridge ports are identified by examining the Bridge MIB and  appropriate ifEntries associated with each 'dot1dBasePort'  and are thus not represented in this table."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.3.3.1.1.
Name: entPhysicalChildIndex(1)
Description: entPhysicalChildIndex OBJECT-TYPE  SYNTAX PhysicalIndex  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of entPhysicalIndex for the contained physical  entity."
----------------------------------------
OID: 1.3.6.1.2.1.47.1.4.1.
Name: entLastChangeTime(1)
Description: entLastChangeTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime at the time a conceptual row is  created, modified, or deleted in any of these tables:  - entPhysicalTable  - entLogicalTable  - entLPMappingTable  - entAliasMappingTable  - entPhysicalContainsTable"
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.1.1.
Name: clogNotificationsSent(1)
Description: clogNotificationsSent OBJECT-TYPE  SYNTAX Counter32  UNITS "notifications"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of clogMessageGenerated notifications that  have been sent. This number may include notifications  that were prevented from being transmitted due to  reasons such as resource limitations and/or  non-connectivity. If one is receiving notifications,  one can periodically poll this object to determine if  any notifications were missed. If so, a poll of the  clogHistoryTable might be appropriate."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.1.2.
Name: N/A
Description: clogNotificationsEnabled OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "Indicates whether clogMessageGenerated notifications  will or will not be sent when a syslog message is  generated by the device. Disabling notifications  does not prevent syslog messages from being added  to the clogHistoryTable."  DEFVAL { false }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.1.3.
Name: clogMaxSeverity(3)
Description: clogMaxSeverity OBJECT-TYPE  SYNTAX SyslogSeverity  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "Indicates which syslog severity levels will be processed. Any syslog message with a severity value greater than this value will be ignored by the agent.  note: severity numeric values increase as their severity decreases, e.g. 'error' is more severe than 'debug'."  DEFVAL {warning}
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.1.4.
Name: clogMsgIgnores(4)
Description: clogMsgIgnores OBJECT-TYPE  SYNTAX Counter32  UNITS "messages"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of syslog messages which were ignored. A  message will be ignored if it has a severity value  greater than clogMaxSeverity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.1.5.
Name: clogMsgDrops(5)
Description: clogMsgDrops OBJECT-TYPE  SYNTAX Counter32  UNITS "messages"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of syslog messages which could not be processed due to lack of system resources. Most likely this will occur at the same time that syslog messages are generated to indicate this lack of resources. Increases in this object's value may serve as an indication that system resource levels should be examined via other mib objects. A message that is dropped will not appear in the history table and no notification will be sent for this message."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.2.1.
Name: N/A
Description: clogHistTableMaxLength OBJECT-TYPE  SYNTAX Integer32 (0..500)  UNITS "entries"  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The upper limit on the number of entries that the  clogHistoryTable may contain. A value of 0 will  prevent any history from being retained. When this  table is full, the oldest entry will be deleted and  a new one will be created."  DEFVAL { 1 }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.2.2.
Name: clogHistMsgsFlushed(2)
Description: clogHistMsgsFlushed OBJECT-TYPE  SYNTAX Counter32  UNITS "messages"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of entries that have been removed from  the clogHistoryTable in order to make room for new  entries. This object can be utilized to determine  whether your polling frequency on the history table  is fast enough and/or the size of your history table  is large enough such that you are not missing  messages."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.2.3.1.2.
Name: clogHistFacility(2)
Description: clogHistFacility OBJECT-TYPE  SYNTAX DisplayString (SIZE (1..20))  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Name of the facility that generated this message.  For example: 'SYS'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.2.3.1.3.
Name: clogHistSeverity(3)
Description: clogHistSeverity OBJECT-TYPE  SYNTAX SyslogSeverity  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The severity of the message."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.2.3.1.4.
Name: clogHistMsgName(4)
Description: clogHistMsgName OBJECT-TYPE  SYNTAX DisplayString (SIZE (1..30))  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A textual identification for the message type.  A facility name in conjunction with a message name uniquely identifies a message type."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.2.3.1.5.
Name: clogHistMsgText(5)
Description: clogHistMsgText OBJECT-TYPE  SYNTAX DisplayString (SIZE (1..255))  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The text of the message. If the text of the message exceeds 255 bytes, the message will be truncated to 254 bytes and a '*' character will be appended - indicating that the message has been truncated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.41.1.2.3.1.6.
Name: clogHistTimestamp(6)
Description: clogHistTimestamp OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime when this message was generated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.48.1.1.1.2.
Name: ciscoMemoryPoolName(2)
Description: ciscoMemoryPoolName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A textual name assigned to the memory pool. This  object is suitable for output to a human operator,  and may also be used to distinguish among the various  pool types, especially among dynamic pools."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.48.1.1.1.3.
Name: N/A
Description: ciscoMemoryPoolAlternate OBJECT-TYPE  SYNTAX Integer32 (0..65535)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates whether or not this memory pool has an  alternate pool configured. Alternate pools are  used for fallback when the current pool runs out  of memory.    If an instance of this object has a value of zero,  then this pool does not have an alternate. Otherwise  the value of this object is the same as the value of  ciscoMemoryPoolType of the alternate pool."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.48.1.1.1.4.
Name: ciscoMemoryPoolValid(4)
Description: ciscoMemoryPoolValid OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates whether or not the remaining objects in  this entry contain accurate data. If an instance  of this object has the value false (which in and of  itself indicates an internal error condition), the  values of the remaining objects in the conceptual row  may contain inaccurate information (specifically, the  reported values may be less than the actual values)."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.48.1.1.1.5.
Name: ciscoMemoryPoolUsed(5)
Description: ciscoMemoryPoolUsed OBJECT-TYPE  SYNTAX Gauge32  UNITS "bytes"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates the number of bytes from the memory pool  that are currently in use by applications on the  managed device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.48.1.1.1.6.
Name: ciscoMemoryPoolFree(6)
Description: ciscoMemoryPoolFree OBJECT-TYPE  SYNTAX Gauge32  UNITS "bytes"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates the number of bytes from the memory pool  that are currently unused on the managed device.    Note that the sum of ciscoMemoryPoolUsed and  ciscoMemoryPoolFree is the total amount of memory  in the pool"
----------------------------------------
OID: 1.3.6.1.4.1.9.9.48.1.1.1.7.
Name: N/A
Description: ciscoMemoryPoolLargestFree OBJECT-TYPE  SYNTAX Gauge32  UNITS "bytes"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates the largest number of contiguous bytes  from the memory pool that are currently unused on  the managed device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.109.1.1.1.1.2.
Name: N/A
Description: cpmCPUTotalPhysicalIndex OBJECT-TYPE  SYNTAX EntPhysicalIndexOrZero  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The entPhysicalIndex of the physical entity for which  the CPU statistics in this entry are maintained.  The physical entity can be a CPU chip, a group of CPUs,  a CPU card etc. The exact type of this entity is described by  its entPhysicalVendorType value. If the CPU statistics  in this entry correspond to more than one physical entity  (or to no physical entity), or if the entPhysicalTable is  not supported on the SNMP agent, the value of this object  must be zero."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.109.1.1.1.1.3.5: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.109.1.1.1.1.3.5
OID: 1.3.6.1.4.1.9.9.109.1.1.1.1.3.5
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.109.1.1.1.1.4.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.109.1.1.1.1.4.1
OID: 1.3.6.1.4.1.9.9.109.1.1.1.1.4.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.109.1.1.1.1.5.5: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.109.1.1.1.1.5.5
OID: 1.3.6.1.4.1.9.9.109.1.1.1.1.5.5
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.1.1.1.1.
Name: N/A
Description: cefcPowerRedundancyMode OBJECT-TYPE  SYNTAX PowerRedundancyType  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The administratively desired power supply redundancy  mode."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.1.1.1.2.
Name: cefcPowerUnits(2)
Description: cefcPowerUnits OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The units of primary supply to interpret  cefcTotalAvailableCurrent and cefcTotalDrawnCurrent  as power.    For example, one 1000-watt power supply could  deliver 100 amperes at 10 volts DC. So the value  of cefcPowerUnits would be 'at 10 volts DC'.    cefcPowerUnits is for display purposes only."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.1.1.1.3.
Name: N/A
Description: cefcTotalAvailableCurrent OBJECT-TYPE  SYNTAX FRUCurrentType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Total current available for FRU usage."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.1.1.1.4.
Name: cefcTotalDrawnCurrent(4)
Description: cefcTotalDrawnCurrent OBJECT-TYPE  SYNTAX FRUCurrentType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Total current drawn by powered-on FRUs."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.1.2.1.1.
Name: N/A
Description: cefcFRUPowerAdminStatus OBJECT-TYPE  SYNTAX PowerAdminType  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "Administratively desired FRU power state."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.1.2.1.2.
Name: N/A
Description: cefcFRUPowerOperStatus OBJECT-TYPE  SYNTAX PowerOperType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Operational FRU power state."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.1.2.1.3.
Name: cefcFRUCurrent(3)
Description: cefcFRUCurrent OBJECT-TYPE  SYNTAX FRUCurrentType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Current supplied by the FRU (positive values)  or current required to operate the FRU (negative values)."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.1.3.
Name: N/A
Description: cefcMaxDefaultInLinePower OBJECT-TYPE  SYNTAX Integer32 (0..12500)  UNITS "miliwatts"  MAX-ACCESS read-write  STATUS deprecated  DESCRIPTION  "The system will provide power to the device connecting  to the FRU if the device needs power, like an IP Phone.  We call the providing power inline power.  This MIB object controls the maximum default inline power  for the device connecting to the FRU in the system. If the  maximum default inline power of the device is greater than  the maximum value reportable by this object, then this  object should report its maximum reportable value (12500)  and cefcMaxDefaultHighInLinePower must be used to report  the actual maximum default inline power."  DEFVAL {12500}
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.2.1.1.1.
Name: cefcModuleAdminStatus(1)
Description: cefcModuleAdminStatus OBJECT-TYPE  SYNTAX ModuleAdminType  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object provides administrative control of the  module."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.2.1.1.2.
Name: cefcModuleOperStatus(2)
Description: cefcModuleOperStatus OBJECT-TYPE  SYNTAX ModuleOperType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This object shows the module's operational state."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.2.1.1.3.
Name: cefcModuleResetReason(3)
Description: cefcModuleResetReason OBJECT-TYPE  SYNTAX ModuleResetReasonType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This object identifies the reason for the last reset performed  on the module."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.2.1.1.4.
Name: N/A
Description: cefcModuleStatusLastChangeTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime at the time the cefcModuleOperStatus  is changed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.117.1.3.1.
Name: N/A
Description: cefcMIBEnableStatusNotification OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This variable indicates whether the system  produces the following notifications:  cefcModuleStatusChange, cefcPowerStatusChange,  cefcFRUInserted, cefcFRURemoved,  cefcUnrecognizedFRU, cefcFanTrayStatusChange  and cefcVmModuleStatusChangeNotif.  A false value will prevent these notifications  from being generated."  DEFVAL {false}
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.1.
Name: N/A
Description: cfwBasicEventsTableLastRow OBJECT-TYPE  SYNTAX Unsigned32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index value of the most recently created row  in the cfwBasicEventsTable. This number starts at  1 and increase by one with each new log entry. When  this number wraps, all events are deleted."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.2.
Name: cfwBasicEventTime(2)
Description: cfwBasicEventTime OBJECT-TYPE  SYNTAX DateAndTime  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The time that the event occurred."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.3.
Name: N/A
Description: cfwBasicSecurityEventType OBJECT-TYPE  SYNTAX SecurityEvent  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of security-related event that this row contains.  If the event is not security-related this object will not  be instantiated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.4.
Name: N/A
Description: cfwBasicContentInspEventType OBJECT-TYPE  SYNTAX ContentInspectionEvent  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of content inspection-related event that this row  contains. If the event is not content inspection-related  this object will not be instantiated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.5.
Name: N/A
Description: cfwBasicConnectionEventType OBJECT-TYPE  SYNTAX ConnectionEvent  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of connection-related event that this row contains.  If the event is not connection-related this object will not  be instantiated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.6.
Name: N/A
Description: cfwBasicAccessEventType OBJECT-TYPE  SYNTAX AccessEvent  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of access-related event that this row contains.  If the event is not access-related this object will not be  instantiated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.7.
Name: N/A
Description: cfwBasicAuthenticationEventType OBJECT-TYPE  SYNTAX AuthenticationEvent  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of authentication-related event that this row  contains. If the event is not authentication-related this  object will not be instantiated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.8.
Name: N/A
Description: cfwBasicGenericEventType OBJECT-TYPE  SYNTAX GenericEvent  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of generic event that this row contains. If the  event does not fall into one of the other categories this  object will be populated. Otherwise, this object will not  be instantiated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.9.
Name: N/A
Description: cfwBasicEventDescription OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A description of the event. The value of the object may  be a zero-length string."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.1.2.1.10.
Name: N/A
Description: cfwBasicEventDetailsTableRow OBJECT-TYPE  SYNTAX RowPointer  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A pointer to a row in the table containing details  about this event. Generally, the table will be the  cfwNetEventsTable but a Cisco-defined table may also  appear here. If there there is no more detailed  information for this event the value of this object  will have the value {0 0}."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.1.
Name: N/A
Description: cfwNetEventsTableLastRow OBJECT-TYPE  SYNTAX Unsigned32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index value of the last row in the  cfwNetEventsTable. This number starts at 1 and  increase by one with each new log entry. When this  number wraps, all events are deleted."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.2.
Name: cfwNetEventInterface(2)
Description: cfwNetEventInterface OBJECT-TYPE  SYNTAX InterfaceIndexOrZero  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The interface most closely associated with this event.  For example, for an event that relates to the receipt of  a packet, this object identifies the interface on which  the packet was received. If there are multiple interfaces  associated with an event, the interface most closely  associated with the cause of the event will be used.  For example, for an event for the setup of a TCP  connection, the interface on the initiator's side  of the connection would be preferred. If there is no  associated interface, then this object has the value zero."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.3.
Name: N/A
Description: cfwNetEventSrcIpAddress OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Source IP address in the IP packet that caused the  event. If there is no packet associated with the  event this object has the value of zero. If the event is  the result of multiple packets with different source  addresses, this value may be zero or an address taken  from an arbitrarily chosen packet in the sequence of  packets causing the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.4.
Name: N/A
Description: cfwNetEventInsideSrcIpAddress OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Source IP address after Network Address Translation  has been applied. If NAT has not been applied to the  source address in this packet this object will not  be instantiated, resulting in a sparse table. If the  event is the result of multiple packets with different  source addresses, this value may be zero or an address  taken from an arbitrarily chosen packet in the sequence  of packets causing the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.5.
Name: N/A
Description: cfwNetEventDstIpAddress OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Destination IP address in the IP packet that caused  the event. If there is no packet associated with  the event this object has the value of zero. If the event  is the result of multiple packets with different destination  addresses, this value may be zero or an address taken  from an arbitrarily chosen packet in the sequence of  packets causing the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.6.
Name: N/A
Description: cfwNetEventInsideDstIpAddress OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Destination IP address after Network Address Translation  has been applied. If NAT has not been applied to the  destination address in this packet this object will not  be instantiated, resulting in a sparse table. If the event  is the result of multiple packets with different destination  addresses, this value may be zero or an address taken  from an arbitrarily chosen packet in the sequence of  packets causing the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.7.
Name: cfwNetEventSrcIpPort(7)
Description: cfwNetEventSrcIpPort OBJECT-TYPE  SYNTAX INTEGER (0..65535)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Source UDP/TCP port in the IP packet that caused  the event. If there is no packet associated with the  event this object has the value of zero. If the event  is the result of multiple packets with different source  ports, this value may be zero or a port taken from an  arbitrarily chosen packet in the sequence of packets  causing the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.8.
Name: N/A
Description: cfwNetEventInsideSrcIpPort OBJECT-TYPE  SYNTAX INTEGER (0..65535)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Source UDP/TCP port after Port Address Translation  has been applied. If PAT has not been applied to the  source port in this packet this object will not be  instantiated, resulting in a sparse table. If the  event is the result of multiple packets with different  source ports, this value may be zero or a port taken  from an arbitrarily chosen packet in the sequence of  packets causing the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.9.
Name: cfwNetEventDstIpPort(9)
Description: cfwNetEventDstIpPort OBJECT-TYPE  SYNTAX INTEGER (0..65535)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Destination UDP/TCP port in the IP packet that caused  the event. If there is no packet associated with the  event this object has the value of zero. If the event is  the result of multiple packets with different destination  ports, this value may be zero or a port taken from an  arbitrarily chosen packet in the sequence of packets  causing the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.10.
Name: N/A
Description: cfwNetEventInsideDstIpPort OBJECT-TYPE  SYNTAX INTEGER (0..65535)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Destination UDP/TCP port after Port Address Translation  has been applied. If PAT has not been applied to the  Destination port in this packet this object will not be  instantiated, resulting in a sparse table. If the event  is the result of multiple packets with different  destination ports, this value may be zero or a port  taken from an arbitrarily chosen packet in the sequence  of packets causing the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.11.
Name: cfwNetEventService(11)
Description: cfwNetEventService OBJECT-TYPE  SYNTAX Services  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The identification of the type of service involved  with this event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.12.
Name: N/A
Description: cfwNetEventServiceInformation OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Specific service information. This can be used to  describe the particular service indentified by  cfwNetEventService and can reflect whether the service  is a local service or a gateway service. For example,  if the value for cfwNetEventService is loginTelnet  then the string provided might be 'local telnet'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.13.
Name: cfwNetEventIdentity(13)
Description: cfwNetEventIdentity OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This object will contain a description of the entity that  caused the event. The entity could be a userid, username,  processid or other identifier for the entity using the service.  If there is no such information then this object will contain  a zero-length string."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.1.2.2.1.14.
Name: N/A
Description: cfwNetEventDescription OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A detailed description of the event."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.2.1.1.1.2.
Name: N/A
Description: cfwHardwareInformation OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A detailed textual description of the resource  identified by cfwHardwareType."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.2.1.1.1.3.
Name: N/A
Description: cfwHardwareStatusValue OBJECT-TYPE  SYNTAX HardwareStatus  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This object contains the current status of the resource."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.2.1.1.1.4.
Name: N/A
Description: cfwHardwareStatusDetail OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A detailed textual description of the current status of  the resource which may provide a more specific description  than cfwHardwareStatusValue."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.2.2.1.1.3.
Name: N/A
Description: cfwBufferStatInformation OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A detailed textual description of the statistic  identified by cfwBufferStatType."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.2.2.1.1.4.
Name: cfwBufferStatValue(4)
Description: cfwBufferStatValue OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the buffer statistic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.2.2.2.1.3.
Name: N/A
Description: cfwConnectionStatDescription OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A detailed textual description of this statistic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.2.2.2.1.4.
Name: N/A
Description: cfwConnectionStatCount OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This is an integer that contains the value of the  resource statistic. If a type of 'gauge' is more  appropriate this object will be omitted resulting  in a sparse table."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.147.1.2.2.2.1.5.
Name: N/A
Description: cfwConnectionStatValue OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This is an integer that contains the value of the  resource statistic. If a type of 'counter' is more  appropriate this object will be omitted resulting  in a sparse table."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.1.1.
Name: cipSecMibLevel(1)
Description: cipSecMibLevel OBJECT-TYPE  SYNTAX Integer32 (1..4096 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The level of the IPsec MIB."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.1.
Name: N/A
Description: cikeGlobalActiveTunnels OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of currently active IPsec  Phase-1 IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.2.
Name: N/A
Description: cikeGlobalPreviousTunnels OBJECT-TYPE  SYNTAX Counter32  UNITS "SAs"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of previously active  IPsec Phase-1 IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.3.
Name: cikeGlobalInOctets(3)
Description: cikeGlobalInOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received by all currently  and previously active IPsec Phase-1 IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.4.
Name: cikeGlobalInPkts(4)
Description: cikeGlobalInPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received by all  currently and previously active IPsec  Phase-1 IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.5.
Name: cikeGlobalInDropPkts(5)
Description: cikeGlobalInDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets which were  dropped during receive processing by all  currently and previously  active IPsec Phase-1 IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.6.
Name: cikeGlobalInNotifys(6)
Description: cikeGlobalInNotifys OBJECT-TYPE  SYNTAX Counter32  UNITS "Notification Payloads"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of notifys received by  all currently and previously active IPsec  Phase-1 IKE Tunnels."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.1.7.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.1.7.2
OID: 1.3.6.1.4.1.9.9.171.1.2.1.7.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.1.8.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.1.8.2
OID: 1.3.6.1.4.1.9.9.171.1.2.1.8.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.1.9.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.1.9.2
OID: 1.3.6.1.4.1.9.9.171.1.2.1.9.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.1.10.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.1.10.2
OID: 1.3.6.1.4.1.9.9.171.1.2.1.10.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.11.
Name: cikeGlobalOutOctets(11)
Description: cikeGlobalOutOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets sent by all currently  and previously active and IPsec Phase-1  IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.12.
Name: cikeGlobalOutPkts(12)
Description: cikeGlobalOutPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets sent by all currently  and previously active and IPsec Phase-1  Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.13.
Name: N/A
Description: cikeGlobalOutDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets which were dropped  during send processing by all currently  and previously  active IPsec Phase-1 IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.14.
Name: cikeGlobalOutNotifys(14)
Description: cikeGlobalOutNotifys OBJECT-TYPE  SYNTAX Counter32  UNITS "Notification Payloads"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of notifys sent by all currently  and previously active IPsec Phase-1 IKE Tunnels."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.1.15.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.1.15.2
OID: 1.3.6.1.4.1.9.9.171.1.2.1.15.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.1.16.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.1.16.2
OID: 1.3.6.1.4.1.9.9.171.1.2.1.16.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.1.17.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.1.17.2
OID: 1.3.6.1.4.1.9.9.171.1.2.1.17.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.1.18.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.1.18.2
OID: 1.3.6.1.4.1.9.9.171.1.2.1.18.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.19.
Name: N/A
Description: cikeGlobalInitTunnels OBJECT-TYPE  SYNTAX Counter32  UNITS "SAs"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of IPsec Phase-1 IKE  Tunnels which were locally initiated."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.20.
Name: N/A
Description: cikeGlobalInitTunnelFails OBJECT-TYPE  SYNTAX Counter32  UNITS "SAs"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of IPsec Phase-1 IKE Tunnels  which were locally initiated and failed to activate."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.21.
Name: N/A
Description: cikeGlobalRespTunnelFails OBJECT-TYPE  SYNTAX Counter32  UNITS "SAs"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of IPsec Phase-1 IKE Tunnels  which were remotely initiated and failed to activate."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.22.
Name: N/A
Description: cikeGlobalSysCapFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of system capacity failures  which occurred during processing of all current  and previously active IPsec Phase-1 IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.23.
Name: cikeGlobalAuthFails(23)
Description: cikeGlobalAuthFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of authentications which ended  in failure by all current and previous IPsec Phase-1  IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.24.
Name: N/A
Description: cikeGlobalDecryptFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of decryptions which ended  in failure by all current and previous IPsec Phase-1  IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.25.
Name: N/A
Description: cikeGlobalHashValidFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of hash validations which ended  in failure by all current and previous IPsec Phase-1  IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.1.26.
Name: cikeGlobalNoSaFails(26)
Description: cikeGlobalNoSaFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of non-existent Security Association  in failures which occurred during processing of  all current and previous IPsec Phase-1 IKE Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.2.1.6.
Name: cikePeerLocalAddr(6)
Description: cikePeerLocalAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the local peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.2.1.7.
Name: cikePeerRemoteAddr(7)
Description: cikePeerRemoteAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the remote peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.2.1.8.
Name: cikePeerActiveTime(8)
Description: cikePeerActiveTime OBJECT-TYPE  SYNTAX TimeInterval  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The length of time that the peer association has  existed in hundredths of a second."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.2.1.9.
Name: N/A
Description: cikePeerActiveTunnelIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the active IPsec Phase-1 IKE Tunnel  (cikeTunIndex in the cikeTunnelTable) for this peer  association. If an IPsec Phase-1 IKE Tunnel is  not currently active, then the value of this  object will be zero."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.2.
Name: cikeTunLocalType(2)
Description: cikeTunLocalType OBJECT-TYPE  SYNTAX IkePeerType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of local peer identity. The local  peer may be identified by:  1. an IP address, or  2. a host name."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.3.
Name: cikeTunLocalValue(3)
Description: cikeTunLocalValue OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the local peer identity.    If the local peer type is an IP Address, then this  is the IP Address used to identify the local peer.    If the local peer type is a host name, then this is  the host name used to identify the local peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.4.
Name: cikeTunLocalAddr(4)
Description: cikeTunLocalAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the local endpoint for the IPsec  Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.5.
Name: cikeTunLocalName(5)
Description: cikeTunLocalName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The DNS name of the local IP address for  the IPsec Phase-1 IKE Tunnel. If the DNS  name associated with the local tunnel endpoint  is not known, then the value of this  object will be a NULL string."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.6.
Name: cikeTunRemoteType(6)
Description: cikeTunRemoteType OBJECT-TYPE  SYNTAX IkePeerType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of remote peer identity.  The remote peer may be identified by:  1. an IP address, or  2. a host name."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.7.
Name: cikeTunRemoteValue(7)
Description: cikeTunRemoteValue OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the remote peer identity.    If the remote peer type is an IP Address, then this  is the IP Address used to identify the remote peer.    If the remote peer type is a host name, then  this is the host name used to identify the  remote peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.8.
Name: cikeTunRemoteAddr(8)
Description: cikeTunRemoteAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the remote endpoint for the IPsec  Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.9.
Name: cikeTunRemoteName(9)
Description: cikeTunRemoteName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The DNS name of the remote IP address of IPsec Phase-1  IKE Tunnel. If the DNS name associated with the remote  tunnel endpoint is not known, then the value of this  object will be a NULL string."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.10.
Name: cikeTunNegoMode(10)
Description: cikeTunNegoMode OBJECT-TYPE  SYNTAX IkeNegoMode  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The negotiation mode of the IPsec Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.11.
Name: N/A
Description: cikeTunDiffHellmanGrp OBJECT-TYPE  SYNTAX DiffHellmanGrp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Diffie Hellman Group used in IPsec Phase-1 IKE  negotiations."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.12.
Name: cikeTunEncryptAlgo(12)
Description: cikeTunEncryptAlgo OBJECT-TYPE  SYNTAX EncryptAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The encryption algorithm used in IPsec Phase-1 IKE  negotiations."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.13.
Name: cikeTunHashAlgo(13)
Description: cikeTunHashAlgo OBJECT-TYPE  SYNTAX IkeHashAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The hash algorithm used in IPsec Phase-1 IKE  negotiations."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.14.
Name: cikeTunAuthMethod(14)
Description: cikeTunAuthMethod OBJECT-TYPE  SYNTAX IkeAuthMethod  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication method used in IPsec Phase-1 IKE  negotiations."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.15.
Name: cikeTunLifeTime(15)
Description: cikeTunLifeTime OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  UNITS "seconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The negotiated LifeTime of the IPsec Phase-1 IKE Tunnel  in seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.16.
Name: cikeTunActiveTime(16)
Description: cikeTunActiveTime OBJECT-TYPE  SYNTAX TimeInterval  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The length of time the IPsec Phase-1 IKE tunnel has been  active in hundredths of seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.17.
Name: N/A
Description: cikeTunSaRefreshThreshold OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  UNITS "seconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The security association refresh threshold in seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.18.
Name: N/A
Description: cikeTunTotalRefreshes OBJECT-TYPE  SYNTAX Counter32  UNITS "QM Exchanges"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of security associations  refreshes performed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.19.
Name: cikeTunInOctets(19)
Description: cikeTunInOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received by  this IPsec Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.20.
Name: cikeTunInPkts(20)
Description: cikeTunInPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received by  this IPsec Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.21.
Name: cikeTunInDropPkts(21)
Description: cikeTunInDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped  by this IPsec Phase-1 IKE Tunnel during  receive processing."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.22.
Name: cikeTunInNotifys(22)
Description: cikeTunInNotifys OBJECT-TYPE  SYNTAX Counter32  UNITS "Notification Payloads"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of notifys received by  this IPsec Phase-1 IKE Tunnel."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.3.1.23.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.3.1.23.2
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.23.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.3.1.24.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.3.1.24.2
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.24.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.3.1.25.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.3.1.25.2
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.25.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.3.1.26.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.3.1.26.2
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.26.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.27.
Name: cikeTunOutOctets(27)
Description: cikeTunOutOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets sent by this IPsec Phase-1  IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.28.
Name: cikeTunOutPkts(28)
Description: cikeTunOutPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets sent by this IPsec Phase-1  IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.29.
Name: cikeTunOutDropPkts(29)
Description: cikeTunOutDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped by this  IPsec Phase-1 IKE Tunnel during send processing."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.30.
Name: cikeTunOutNotifys(30)
Description: cikeTunOutNotifys OBJECT-TYPE  SYNTAX Counter32  UNITS "Notification Payloads"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of notifys sent by this  IPsec Phase-1 Tunnel."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.3.1.31.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.3.1.31.2
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.31.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.3.1.32.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.3.1.32.2
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.32.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.3.1.33.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.3.1.33.2
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.33.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.2.3.1.34.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.2.3.1.34.2
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.34.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.3.1.35.
Name: cikeTunStatus(35)
Description: cikeTunStatus OBJECT-TYPE  SYNTAX TunnelStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The status of the MIB table row.    This object can be used to bring the tunnel down  by setting value of this object to destroy(2).    This object cannot be used to create  a MIB table row."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.2.4.1.7.
Name: N/A
Description: cikePeerCorrIpSecTunIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the active IPsec Phase-2 Tunnel  (cipSecTunIndex in the cipSecTunnelTable) for this  IPsec Phase-1 IKE Peer Association."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.1.
Name: N/A
Description: cipSecGlobalActiveTunnels OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of currently active  IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.2.
Name: N/A
Description: cipSecGlobalPreviousTunnels OBJECT-TYPE  SYNTAX Counter32  UNITS "Phase-2 Tunnels"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of previously active  IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.3.
Name: cipSecGlobalInOctets(3)
Description: cipSecGlobalInOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received by all  current and previous IPsec Phase-2 Tunnels.  This value is  accumulated BEFORE determining whether or not  the packet should be decompressed. See also  cipSecGlobalInOctWraps for the number of times  this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.4.
Name: N/A
Description: cipSecGlobalHcInOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number of  octets received by all current and previous  IPsec Phase-2 Tunnels. This value is accumulated  BEFORE determining whether or not the packet  should be decompressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.5.
Name: N/A
Description: cipSecGlobalInOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the global octets received  counter (cipSecGlobalInOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.6.
Name: N/A
Description: cipSecGlobalInDecompOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of decompressed octets received  by all current and previous IPsec Phase-2 Tunnels.  This value is accumulated AFTER the packet is  decompressed. If compression is not being used,  this value will match the value of cipSecGlobalInOctets.  See also cipSecGlobalInDecompOctWraps  for the number of times this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.7.
Name: N/A
Description: cipSecGlobalHcInDecompOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number  of decompressed octets received by all current  and previous IPsec Phase-2 Tunnels. This value  is accumulated AFTER the packet is decompressed.  If compression is not being used, this value  will match the value of cipSecGlobalHcInOctets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.8.
Name: N/A
Description: cipSecGlobalInDecompOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the global decompressed  octets received counter  (cipSecGlobalInDecompOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.9.
Name: cipSecGlobalInPkts(9)
Description: cipSecGlobalInPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received  by all current and previous  IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.10.
Name: cipSecGlobalInDrops(10)
Description: cipSecGlobalInDrops OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped  during receive processing by all current and previous  IPsec Phase-2 Tunnels. This count does  NOT include packets dropped due to  Anti-Replay processing."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.11.
Name: N/A
Description: cipSecGlobalInReplayDrops OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped during  receive processing due to Anti-Replay  processing by all current and previous IPsec  Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.12.
Name: cipSecGlobalInAuths(12)
Description: cipSecGlobalInAuths OBJECT-TYPE  SYNTAX Counter32  UNITS "Events"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound authentication's  performed by all current and previous IPsec  Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.13.
Name: N/A
Description: cipSecGlobalInAuthFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound authentication's  which ended in failure by all current and previous  IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.14.
Name: N/A
Description: cipSecGlobalInDecrypts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound decryption's  performed by all current and previous IPsec  Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.15.
Name: N/A
Description: cipSecGlobalInDecryptFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound decryption's  which ended in failure by all current and  previous IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.16.
Name: N/A
Description: cipSecGlobalOutOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets sent by all  current and previous IPsec Phase-2 Tunnels.  This value is accumulated AFTER determining  whether or not the packet should be compressed.  See also cipSecGlobalOutOctWraps for the  number of times this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.17.
Name: N/A
Description: cipSecGlobalHcOutOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number  of octets sent by all current and previous  IPsec Phase-2 Tunnels. This value is accumulated  AFTER determining whether or not the packet should  be compressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.18.
Name: N/A
Description: cipSecGlobalOutOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the global octets sent counter  (cipSecGlobalOutOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.19.
Name: N/A
Description: cipSecGlobalOutUncompOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of uncompressed octets sent  by all current and previous IPsec Phase-2 Tunnels.  This value is accumulated BEFORE the packet is  compressed. If compression is not being used, this  value will match the value of cipSecGlobalOutOctets.  See also cipSecGlobalOutDecompOctWraps for the number  of times this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.20.
Name: N/A
Description: cipSecGlobalHcOutUncompOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number of  uncompressed octets sent by all current and previous  IPsec Phase-2 Tunnels. This value is accumulated  BEFORE the packet is compressed. If compression is  not being used, this value will match the  value of cipSecGlobalHcOutOctets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.21.
Name: N/A
Description: cipSecGlobalOutUncompOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the global uncompressed  octets sent counter (cipSecGlobalOutUncompOctets)  has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.22.
Name: cipSecGlobalOutPkts(22)
Description: cipSecGlobalOutPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets sent by all  current and previous  IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.23.
Name: cipSecGlobalOutDrops(23)
Description: cipSecGlobalOutDrops OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped during send  processing by all current and previous IPsec  Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.24.
Name: cipSecGlobalOutAuths(24)
Description: cipSecGlobalOutAuths OBJECT-TYPE  SYNTAX Counter32  UNITS "Events"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound authentication's  performed by all current and previous IPsec  Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.25.
Name: N/A
Description: cipSecGlobalOutAuthFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound authentication's  which ended in failure  by all current and previous IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.26.
Name: N/A
Description: cipSecGlobalOutEncrypts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound encryption's performed  by all current and previous IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.27.
Name: N/A
Description: cipSecGlobalOutEncryptFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound encryption's  which ended in failure by all current and  previous IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.28.
Name: N/A
Description: cipSecGlobalProtocolUseFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of protocol use failures  which occurred during processing of all current  and previously active IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.29.
Name: N/A
Description: cipSecGlobalNoSaFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of non-existent  Security Association in failures which occurred  during processing of all current  and previous IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.1.30.
Name: N/A
Description: cipSecGlobalSysCapFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of system capacity failures  which occurred during processing of all current  and previously active IPsec Phase-2 Tunnels."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.2.
Name: N/A
Description: cipSecTunIkeTunnelIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the associated IPsec Phase-1  IKE Tunnel.  (cikeTunIndex in the cikeTunnelTable)"
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.3.
Name: N/A
Description: cipSecTunIkeTunnelAlive OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "An indicator which specifies whether or not the  IPsec Phase-1 IKE Tunnel currently exists."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.4.
Name: cipSecTunLocalAddr(4)
Description: cipSecTunLocalAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the local endpoint for the IPsec  Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.5.
Name: cipSecTunRemoteAddr(5)
Description: cipSecTunRemoteAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the remote endpoint for the IPsec  Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.6.
Name: cipSecTunKeyType(6)
Description: cipSecTunKeyType OBJECT-TYPE  SYNTAX KeyType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of key used by the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.7.
Name: cipSecTunEncapMode(7)
Description: cipSecTunEncapMode OBJECT-TYPE  SYNTAX EncapMode  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The encapsulation mode used by the  IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.8.
Name: cipSecTunLifeSize(8)
Description: cipSecTunLifeSize OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  UNITS "KBytes"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The negotiated LifeSize of the  IPsec Phase-2 Tunnel in kilobytes."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.9.
Name: cipSecTunLifeTime(9)
Description: cipSecTunLifeTime OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  UNITS "Seconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The negotiated LifeTime of the  IPsec Phase-2 Tunnel in seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.10.
Name: cipSecTunActiveTime(10)
Description: cipSecTunActiveTime OBJECT-TYPE  SYNTAX TimeInterval  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The length of time the IPsec Phase-2  Tunnel has been  active in hundredths of seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.11.
Name: N/A
Description: cipSecTunSaLifeSizeThreshold OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  UNITS "KBytes"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The security association LifeSize refresh  threshold in kilobytes."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.12.
Name: N/A
Description: cipSecTunSaLifeTimeThreshold OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  UNITS "Seconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The security association LifeTime refresh  threshold in seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.13.
Name: N/A
Description: cipSecTunTotalRefreshes OBJECT-TYPE  SYNTAX Counter32  UNITS "QM Exchanges"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of security  association refreshes performed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.14.
Name: N/A
Description: cipSecTunExpiredSaInstances OBJECT-TYPE  SYNTAX Counter32  UNITS "SAs"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of security associations  which have expired."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.15.
Name: N/A
Description: cipSecTunCurrentSaInstances OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of security associations  which are currently active or expiring."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.16.
Name: N/A
Description: cipSecTunInSaDiffHellmanGrp OBJECT-TYPE  SYNTAX DiffHellmanGrp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Diffie Hellman Group used  by the inbound security association of the  IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.17.
Name: N/A
Description: cipSecTunInSaEncryptAlgo OBJECT-TYPE  SYNTAX EncryptAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The encryption algorithm used by the inbound security  association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.18.
Name: N/A
Description: cipSecTunInSaAhAuthAlgo OBJECT-TYPE  SYNTAX AuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication algorithm used by the inbound  authentication header (AH) security association of  the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.19.
Name: N/A
Description: cipSecTunInSaEspAuthAlgo OBJECT-TYPE  SYNTAX AuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication algorithm used by the inbound  encapsulation security protocol (ESP) security  association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.20.
Name: N/A
Description: cipSecTunInSaDecompAlgo OBJECT-TYPE  SYNTAX CompAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The decompression algorithm used by the inbound  security association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.21.
Name: N/A
Description: cipSecTunOutSaDiffHellmanGrp OBJECT-TYPE  SYNTAX DiffHellmanGrp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Diffie Hellman Group used by the outbound security  association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.22.
Name: N/A
Description: cipSecTunOutSaEncryptAlgo OBJECT-TYPE  SYNTAX EncryptAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The encryption algorithm used by the outbound security  association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.23.
Name: N/A
Description: cipSecTunOutSaAhAuthAlgo OBJECT-TYPE  SYNTAX AuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication algorithm used by the outbound  authentication header (AH) security association of  the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.24.
Name: N/A
Description: cipSecTunOutSaEspAuthAlgo OBJECT-TYPE  SYNTAX AuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication algorithm used by the inbound  encapsulation security protocol (ESP)  security association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.25.
Name: N/A
Description: cipSecTunOutSaCompAlgo OBJECT-TYPE  SYNTAX CompAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The compression algorithm used by the inbound  security association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.26.
Name: cipSecTunInOctets(26)
Description: cipSecTunInOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received by this IPsec  Phase-2 Tunnel. This value is accumulated  BEFORE determining whether or not the packet should be  decompressed. See also cipSecTunInOctWraps for the  number of times this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.27.
Name: cipSecTunHcInOctets(27)
Description: cipSecTunHcInOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number of octets  received by this IPsec Phase-2 Tunnel. This value is  accumulated BEFORE determining whether or not the packet  should be decompressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.28.
Name: cipSecTunInOctWraps(28)
Description: cipSecTunInOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the octets received counter  (cipSecTunInOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.29.
Name: N/A
Description: cipSecTunInDecompOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of decompressed octets received  by this IPsec Phase-2 Tunnel. This value is  accumulated AFTER the packet is decompressed.  If compression is not being  used, this value will match the value of  cipSecTunInOctets. See also cipSecTunInDecompOctWraps  for the number of times  this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.30.
Name: N/A
Description: cipSecTunHcInDecompOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number of decompressed  octets received by this IPsec Phase-2 Tunnel. This value  is accumulated AFTER the packet is decompressed. If  compression is not being used, this value will match the  value of cipSecTunHcInOctets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.31.
Name: N/A
Description: cipSecTunInDecompOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the decompressed  octets received counter  (cipSecTunInDecompOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.32.
Name: cipSecTunInPkts(32)
Description: cipSecTunInPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.33.
Name: cipSecTunInDropPkts(33)
Description: cipSecTunInDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped  during receive processing by this IPsec Phase-2  Tunnel. This count does NOT include  packets dropped due to Anti-Replay processing."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.34.
Name: N/A
Description: cipSecTunInReplayDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped during  receive processing due to Anti-Replay processing  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.35.
Name: cipSecTunInAuths(35)
Description: cipSecTunInAuths OBJECT-TYPE  SYNTAX Counter32  UNITS "Events"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound  authentication's performed by this  IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.36.
Name: cipSecTunInAuthFails(36)
Description: cipSecTunInAuthFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound authentication's  which ended in  failure by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.37.
Name: cipSecTunInDecrypts(37)
Description: cipSecTunInDecrypts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound decryption's performed  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.38.
Name: N/A
Description: cipSecTunInDecryptFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound decryption's  which ended in failure  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.39.
Name: cipSecTunOutOctets(39)
Description: cipSecTunOutOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets sent by this IPsec  Phase-2 Tunnel. This value is accumulated  AFTER determining whether or not the packet should  be compressed. See also cipSecTunOutOctWraps for  the number of times this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.40.
Name: cipSecTunHcOutOctets(40)
Description: cipSecTunHcOutOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number of octets  sent by this IPsec Phase-2 Tunnel. This value is  accumulated AFTER determining whether or not the  packet  should be compressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.41.
Name: cipSecTunOutOctWraps(41)
Description: cipSecTunOutOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the out octets counter  (cipSecTunOutOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.42.
Name: N/A
Description: cipSecTunOutUncompOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of uncompressed octets sent  by this IPsec Phase-2 Tunnel. This value  is accumulated BEFORE the packet is compressed.  If compression is not being used, this value  will match the value of cipSecTunOutOctets.  See also cipSecTunOutDecompOctWraps for the  number of times this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.43.
Name: N/A
Description: cipSecTunHcOutUncompOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number  of uncompressed octets sent by this IPsec  Phase-2 Tunnel. This value is accumulated BEFORE  the packet is compressed. If compression  is not being used, this value will match the value  of cipSecTunHcOutOctets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.44.
Name: N/A
Description: cipSecTunOutUncompOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the uncompressed octets sent  counter (cipSecTunOutUncompOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.45.
Name: cipSecTunOutPkts(45)
Description: cipSecTunOutPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets sent by this  IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.46.
Name: cipSecTunOutDropPkts(46)
Description: cipSecTunOutDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped during  send processing by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.47.
Name: cipSecTunOutAuths(47)
Description: cipSecTunOutAuths OBJECT-TYPE  SYNTAX Counter32  UNITS "Events"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound authentication's performed  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.48.
Name: N/A
Description: cipSecTunOutAuthFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound  authentication's which ended in failure  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.49.
Name: cipSecTunOutEncrypts(49)
Description: cipSecTunOutEncrypts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound encryption's performed  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.50.
Name: N/A
Description: cipSecTunOutEncryptFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound encryption's  which ended in failure by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.2.1.51.
Name: cipSecTunStatus(51)
Description: cipSecTunStatus OBJECT-TYPE  SYNTAX TunnelStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The status of the MIB table row.    This object can be used to bring the tunnel down  by setting value of this object to destroy(2).  When the value is set to destroy(2), the SA  bundle is destroyed and this row is deleted  from this table.    When this MIB value is queried, the value of  active(1) is always returned, if the instance  exists.    This object cannot be used to create a MIB  table row."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.2.
Name: cipSecEndPtLocalName(2)
Description: cipSecEndPtLocalName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The DNS name of the local Endpoint."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.3.
Name: cipSecEndPtLocalType(3)
Description: cipSecEndPtLocalType OBJECT-TYPE  SYNTAX EndPtType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of identity for the local Endpoint.  Possible values are:  1) a single IP address, or  2) an IP address range, or  3) an IP subnet."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.3.3.1.4.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.3.3.1.4.1
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.4.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.3.3.1.5.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.3.3.1.5.2
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.5.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.6.
Name: N/A
Description: cipSecEndPtLocalProtocol OBJECT-TYPE  SYNTAX Integer32 (0..255 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The protocol number of the local Endpoint's traffic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.7.
Name: cipSecEndPtLocalPort(7)
Description: cipSecEndPtLocalPort OBJECT-TYPE  SYNTAX Integer32 (0..65535 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The port number of the local Endpoint's traffic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.8.
Name: cipSecEndPtRemoteName(8)
Description: cipSecEndPtRemoteName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The DNS name of the remote Endpoint."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.9.
Name: cipSecEndPtRemoteType(9)
Description: cipSecEndPtRemoteType OBJECT-TYPE  SYNTAX EndPtType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of identity for the remote Endpoint.  Possible values are:  1) a single IP address, or  2) an IP address range, or  3) an IP subnet."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.3.3.1.10.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.3.3.1.10.1
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.10.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.3.3.1.11.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.3.3.1.11.2
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.11.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.12.
Name: N/A
Description: cipSecEndPtRemoteProtocol OBJECT-TYPE  SYNTAX Integer32 (0..255 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The protocol number of the remote Endpoint's traffic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.3.1.13.
Name: N/A
Description: cipSecEndPtRemotePort OBJECT-TYPE  SYNTAX Integer32 (0..65535 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The port number of the remote Endpoint's traffic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.4.1.2.
Name: cipSecSpiDirection(2)
Description: cipSecSpiDirection OBJECT-TYPE  SYNTAX INTEGER {  in(1),  out(2)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The direction of the SPI."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.4.1.3.
Name: cipSecSpiValue(3)
Description: cipSecSpiValue OBJECT-TYPE  SYNTAX Unsigned32 (1..4294967295 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the SPI."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.4.1.4.
Name: cipSecSpiProtocol(4)
Description: cipSecSpiProtocol OBJECT-TYPE  SYNTAX INTEGER {  ah(1),  esp(2),  ipcomp(3)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The protocol of the SPI."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.3.4.1.5.
Name: cipSecSpiStatus(5)
Description: cipSecSpiStatus OBJECT-TYPE  SYNTAX INTEGER {  active(1),  expiring(2)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The status of the SPI."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.1.1.1.
Name: cipSecHistTableSize(1)
Description: cipSecHistTableSize OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The window size of the IPsec Phase-1 and Phase-2  History Tables.    The IPsec Phase-1 and Phase-2 History Tables are  implemented as a sliding window in which only the  last n entries are maintained. This object is used  specify the number of entries which will be  maintained in the IPsec Phase-1 and  Phase-2 History Tables.    An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.1.1.2.
Name: cipSecHistCheckPoint(2)
Description: cipSecHistCheckPoint OBJECT-TYPE  SYNTAX INTEGER {  ready(1),  checkPoint(2)  }  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The current state of check point processing.    This object will return ready when the agent is  ready to create on-demand history entries for  active IPsec Tunnels or checkPoint when the  agent is currently creating on-demand history  entries for active IPsec Tunnels.    By setting this value to checkPoint, the agent  will create:  a) an entry in the IPsec Phase-1 Tunnel History  for each active IPsec Phase-1 Tunnel and  b) an entry in the IPsec Phase-2 Tunnel History  Table and an entry in the IPsec Phase-2  Tunnel EndPoint History Table  for each active IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.2.
Name: cikeTunHistTermReason(2)
Description: cikeTunHistTermReason OBJECT-TYPE  SYNTAX INTEGER {  other(1),  normal(2),  operRequest(3),  peerDelRequest(4),  peerLost(5),  localFailure(6),  checkPointReg(7)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The reason the IPsec Phase-1 IKE Tunnel was terminated.  Possible reasons include:  1 = other  2 = normal termination  3 = operator request  4 = peer delete request was received  5 = contact with peer was lost  6 = local failure occurred.  7 = operator initiated check point request"
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.3.
Name: N/A
Description: cikeTunHistActiveIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the previously active IPsec  Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.4.
Name: N/A
Description: cikeTunHistPeerLocalType OBJECT-TYPE  SYNTAX IkePeerType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of local peer identity. The local peer  may be identified by:  1. an IP address, or  2. a host name."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.5.
Name: N/A
Description: cikeTunHistPeerLocalValue OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the local peer identity.    If the local peer type is an IP Address, then this  is the IP Address used to identify the local peer.    If the local peer type is a host name, then this is  the host name used to identify the local peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.6.
Name: N/A
Description: cikeTunHistPeerIntIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The internal index of the local-remote peer  association. This internal index is used to  uniquely identify multiple associations between  the local and remote peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.7.
Name: N/A
Description: cikeTunHistPeerRemoteType OBJECT-TYPE  SYNTAX IkePeerType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of remote peer identity. The remote  peer may be identified by:  1. an IP address, or  2. a host name."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.8.
Name: N/A
Description: cikeTunHistPeerRemoteValue OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the remote peer identity.    If the remote peer type is an IP Address, then this  is the IP Address used to identify the remote peer.    If the remote peer type is a host name, then this is  the host name used to identify the remote peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.9.
Name: cikeTunHistLocalAddr(9)
Description: cikeTunHistLocalAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the local endpoint for the IPsec  Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.10.
Name: cikeTunHistLocalName(10)
Description: cikeTunHistLocalName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The DNS name of the local IP address for  the IPsec Phase-1 IKE Tunnel. If the DNS  name associated with the local tunnel endpoint  is not known, then the value of this  object will be a NULL string."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.11.
Name: N/A
Description: cikeTunHistRemoteAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the remote endpoint for the IPsec  Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.12.
Name: N/A
Description: cikeTunHistRemoteName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The DNS name of the remote IP address of IPsec Phase-1  IKE Tunnel. If the DNS name associated with the remote  tunnel endpoint is not known, then the value of this  object will be a NULL string."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.13.
Name: cikeTunHistNegoMode(13)
Description: cikeTunHistNegoMode OBJECT-TYPE  SYNTAX IkeNegoMode  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The negotiation mode of the IPsec Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.14.
Name: N/A
Description: cikeTunHistDiffHellmanGrp OBJECT-TYPE  SYNTAX DiffHellmanGrp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Diffie Hellman Group used in IPsec Phase-1 IKE  negotiations."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.15.
Name: N/A
Description: cikeTunHistEncryptAlgo OBJECT-TYPE  SYNTAX EncryptAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The encryption algorithm used in IPsec Phase-1 IKE  negotiations."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.16.
Name: cikeTunHistHashAlgo(16)
Description: cikeTunHistHashAlgo OBJECT-TYPE  SYNTAX IkeHashAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The hash algorithm used in IPsec Phase-1 IKE  negotiations."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.17.
Name: N/A
Description: cikeTunHistAuthMethod OBJECT-TYPE  SYNTAX IkeAuthMethod  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication method used in IPsec Phase-1 IKE  negotiations."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.18.
Name: cikeTunHistLifeTime(18)
Description: cikeTunHistLifeTime OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The negotiated LifeTime of the IPsec Phase-1 IKE Tunnel  in seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.19.
Name: cikeTunHistStartTime(19)
Description: cikeTunHistStartTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime in hundredths of seconds  when the IPsec Phase-1 IKE tunnel was started."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.20.
Name: N/A
Description: cikeTunHistActiveTime OBJECT-TYPE  SYNTAX TimeInterval  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The length of time the IPsec Phase-1 IKE tunnel was been  active in hundredths of seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.21.
Name: N/A
Description: cikeTunHistTotalRefreshes OBJECT-TYPE  SYNTAX Counter32  UNITS "QM Exchanges"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of security associations  refreshes performed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.22.
Name: cikeTunHistTotalSas(22)
Description: cikeTunHistTotalSas OBJECT-TYPE  SYNTAX Counter32  UNITS "SAs"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of security associations  used during the  life of the IPsec Phase-1 IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.23.
Name: cikeTunHistInOctets(23)
Description: cikeTunHistInOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets  received by this IPsec Phase-1  IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.24.
Name: cikeTunHistInPkts(24)
Description: cikeTunHistInPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received  by this IPsec Phase-1  IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.25.
Name: N/A
Description: cikeTunHistInDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped  by this IPsec Phase-1  IKE Tunnel during receive processing."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.26.
Name: cikeTunHistInNotifys(26)
Description: cikeTunHistInNotifys OBJECT-TYPE  SYNTAX Counter32  UNITS "Notification Payloads"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of notifys received  by this IPsec Phase-1  IKE Tunnel."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.2.1.1.27.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.2.1.1.27.2
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.27.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.2.1.1.28.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.2.1.1.28.2
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.28.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.2.1.1.29.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.2.1.1.29.2
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.29.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.2.1.1.30.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.2.1.1.30.2
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.30.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.31.
Name: cikeTunHistOutOctets(31)
Description: cikeTunHistOutOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets sent by this IPsec Phase-1  IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.32.
Name: cikeTunHistOutPkts(32)
Description: cikeTunHistOutPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets sent by this IPsec Phase-1  IKE Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.33.
Name: N/A
Description: cikeTunHistOutDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped  by this IPsec Phase-1  IKE Tunnel during send processing."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.34.
Name: N/A
Description: cikeTunHistOutNotifys OBJECT-TYPE  SYNTAX Counter32  UNITS "Notification Payloads"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of notifys sent by this IPsec Phase-1  IKE Tunnel."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.2.1.1.35.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.2.1.1.35.2
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.35.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.2.1.1.36.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.2.1.1.36.2
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.36.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.2.1.1.37.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.2.1.1.37.2
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.37.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.2.1.1.38.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.2.1.1.38.2
OID: 1.3.6.1.4.1.9.9.171.1.4.2.1.1.38.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.2.
Name: N/A
Description: cipSecTunHistTermReason OBJECT-TYPE  SYNTAX INTEGER {  other(1),  normal(2),  operRequest(3),  peerDelRequest(4),  peerLost(5),  seqNumRollOver(6),  checkPointReq(7)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The reason the IPsec Phase-2 Tunnel was terminated.  Possible reasons include:  1 = other  2 = normal termination  3 = operator request  4 = peer delete request was received  5 = contact with peer was lost  6 = local failure occurred  7 = operator initiated check point request"
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.3.
Name: N/A
Description: cipSecTunHistActiveIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the previously active  IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.4.
Name: N/A
Description: cipSecTunHistIkeTunnelIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the associated IPsec Phase-1 Tunnel  (cikeTunIndex in the cikeTunnelTable)."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.5.
Name: N/A
Description: cipSecTunHistLocalAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the local endpoint for the IPsec  Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.6.
Name: N/A
Description: cipSecTunHistRemoteAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the remote endpoint for the IPsec  Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.7.
Name: cipSecTunHistKeyType(7)
Description: cipSecTunHistKeyType OBJECT-TYPE  SYNTAX KeyType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of key used by the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.8.
Name: N/A
Description: cipSecTunHistEncapMode OBJECT-TYPE  SYNTAX EncapMode  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The encapsulation mode used by the  IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.9.
Name: cipSecTunHistLifeSize(9)
Description: cipSecTunHistLifeSize OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  UNITS "KBytes"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The negotiated LifeSize of the IPsec Phase-2 Tunnel in  kilobytes."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.10.
Name: N/A
Description: cipSecTunHistLifeTime OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  UNITS "Seconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The negotiated LifeTime of the IPsec Phase-2 Tunnel in  seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.11.
Name: N/A
Description: cipSecTunHistStartTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime in hundredths of seconds  when the IPsec Phase-2 Tunnel was started."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.12.
Name: N/A
Description: cipSecTunHistActiveTime OBJECT-TYPE  SYNTAX TimeInterval  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The length of time the IPsec Phase-2 Tunnel has been  active in hundredths of seconds."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.13.
Name: N/A
Description: cipSecTunHistTotalRefreshes OBJECT-TYPE  SYNTAX Counter32  UNITS "QM Exchanges"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of security association refreshes  performed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.14.
Name: N/A
Description: cipSecTunHistTotalSas OBJECT-TYPE  SYNTAX Counter32  UNITS "SAs"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of security associations used  during the  life of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.15.
Name: N/A
Description: cipSecTunHistInSaDiffHellmanGrp OBJECT-TYPE  SYNTAX DiffHellmanGrp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Diffie Hellman Group used by the inbound security  association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.16.
Name: N/A
Description: cipSecTunHistInSaEncryptAlgo OBJECT-TYPE  SYNTAX EncryptAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The encryption algorithm used by the inbound security  association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.17.
Name: N/A
Description: cipSecTunHistInSaAhAuthAlgo OBJECT-TYPE  SYNTAX AuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication algorithm used by the inbound  authentication header (AH) security association of  the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.18.
Name: N/A
Description: cipSecTunHistInSaEspAuthAlgo OBJECT-TYPE  SYNTAX AuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication algorithm used by the inbound  encapsulation security protocol (ESP)  security association of  the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.19.
Name: N/A
Description: cipSecTunHistInSaDecompAlgo OBJECT-TYPE  SYNTAX CompAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The decompression algorithm used by the inbound  security association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.20.
Name: N/A
Description: cipSecTunHistOutSaDiffHellmanGrp OBJECT-TYPE  SYNTAX DiffHellmanGrp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Diffie Hellman Group used by the outbound security  association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.21.
Name: N/A
Description: cipSecTunHistOutSaEncryptAlgo OBJECT-TYPE  SYNTAX EncryptAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The encryption algorithm used by the outbound security  association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.22.
Name: N/A
Description: cipSecTunHistOutSaAhAuthAlgo OBJECT-TYPE  SYNTAX AuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication algorithm used by the outbound  authentication header (AH) security association of  the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.23.
Name: N/A
Description: cipSecTunHistOutSaEspAuthAlgo OBJECT-TYPE  SYNTAX AuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The authentication algorithm used by the inbound  encapsulation security protocol (ESP)  security association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.24.
Name: N/A
Description: cipSecTunHistOutSaCompAlgo OBJECT-TYPE  SYNTAX CompAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The compression algorithm used by the inbound  security association of the IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.25.
Name: N/A
Description: cipSecTunHistInOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received by this IPsec  Phase-2 Tunnel. This value is accumulated  BEFORE determining whether or not the packet should  be decompressed. See also cipSecTunInOctWraps for  the number of times this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.26.
Name: N/A
Description: cipSecTunHistHcInOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number of octets  received by this IPsec Phase-2 Tunnel. This value is  accumulated BEFORE determining whether or not  the packet should be decompressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.27.
Name: N/A
Description: cipSecTunHistInOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the octets received counter  (cipSecTunInOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.28.
Name: N/A
Description: cipSecTunHistInDecompOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of decompressed octets received by this  IPsec Phase-2 Tunnel. This value is accumulated AFTER  the packet is decompressed. If compression is not being  used, this value will match the value of cipSecTunHistInOctets.  See also cipSecTunInDecompOctWraps for the number of times  this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.29.
Name: N/A
Description: cipSecTunHistHcInDecompOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number of decompressed  octets received by this IPsec Phase-2 Tunnel. This value  is accumulated AFTER the packet is decompressed. If  compression is not being used, this value will match the  value of cipSecTunHistHcInOctets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.30.
Name: N/A
Description: cipSecTunHistInDecompOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the decompressed octets  received counter (cipSecTunInDecompOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.31.
Name: cipSecTunHistInPkts(31)
Description: cipSecTunHistInPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received by this  IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.32.
Name: N/A
Description: cipSecTunHistInDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped during  receive processing by this IPsec Phase-2 Tunnel.  This count does NOT include packets  dropped due to Anti-Replay processing."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.33.
Name: N/A
Description: cipSecTunHistInReplayDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped during  receive processing due to Anti-Replay processing  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.34.
Name: cipSecTunHistInAuths(34)
Description: cipSecTunHistInAuths OBJECT-TYPE  SYNTAX Counter32  UNITS "Events"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound authentication's  performed  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.35.
Name: N/A
Description: cipSecTunHistInAuthFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound authentication's  which ended in  failure by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.36.
Name: N/A
Description: cipSecTunHistInDecrypts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound decryption's performed  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.37.
Name: N/A
Description: cipSecTunHistInDecryptFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of inbound decryption's  which ended in failure  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.38.
Name: N/A
Description: cipSecTunHistOutOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets sent by this IPsec  Phase-2 Tunnel. This value is accumulated  AFTER determining whether or not the  packet should be  compressed. See also cipSecTunOutOctWraps for the  number of times this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.39.
Name: N/A
Description: cipSecTunHistHcOutOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total number of octets  sent by this IPsec Phase-2 Tunnel. This value  is accumulated AFTER determining whether or not  the packet should be  compressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.40.
Name: N/A
Description: cipSecTunHistOutOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the octets sent counter  (cipSecTunOutOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.41.
Name: N/A
Description: cipSecTunHistOutUncompOctets OBJECT-TYPE  SYNTAX Counter32  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of uncompressed octets sent by this  IPsec Phase-2 Tunnel. This value is accumulated BEFORE  the packet is compressed. If compression is not being  used, this value will match the value of  cipSecTunHistOutOctets. See also  cipSecTunOutDecompOctWraps for the number of times  this counter has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.42.
Name: N/A
Description: cipSecTunHistHcOutUncompOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A high capacity count of the total  number of uncompressed octets sent by this  IPsec Phase-2 Tunnel. This value is accumulated  BEFORE the packet is compressed. If compression  is not being used, this value will match the value of  cipSecTunHistHcOutOctets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.43.
Name: N/A
Description: cipSecTunHistOutUncompOctWraps OBJECT-TYPE  SYNTAX Counter32  UNITS "Integral units"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the uncompressed octets sent counter  (cipSecTunOutUncompOctets) has wrapped."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.44.
Name: cipSecTunHistOutPkts(44)
Description: cipSecTunHistOutPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets sent by this  IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.45.
Name: N/A
Description: cipSecTunHistOutDropPkts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped  during send processing  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.46.
Name: N/A
Description: cipSecTunHistOutAuths OBJECT-TYPE  SYNTAX Counter32  UNITS "Events"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound authentication's performed  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.47.
Name: N/A
Description: cipSecTunHistOutAuthFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound authentication's  which ended in  failure by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.48.
Name: N/A
Description: cipSecTunHistOutEncrypts OBJECT-TYPE  SYNTAX Counter32  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound encryption's performed  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.1.1.49.
Name: N/A
Description: cipSecTunHistOutEncryptFails OBJECT-TYPE  SYNTAX Counter32  UNITS "Failures"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outbound encryption's  which ended in failure  by this IPsec Phase-2 Tunnel."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.2.
Name: N/A
Description: cipSecEndPtHistTunIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the previously active IPsec  Phase-2 Tunnel Table."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.3.
Name: N/A
Description: cipSecEndPtHistActiveIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the previously active Endpoint."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.4.
Name: N/A
Description: cipSecEndPtHistLocalName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The DNS name of the local Endpoint."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.5.
Name: N/A
Description: cipSecEndPtHistLocalType OBJECT-TYPE  SYNTAX EndPtType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of identity for the local Endpoint.  Possible values are:  1) a single IP address, or  2) an IP address range, or  3) an IP subnet."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.3.2.1.6.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.3.2.1.6.1
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.6.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.3.2.1.7.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.3.2.1.7.2
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.7.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.8.
Name: N/A
Description: cipSecEndPtHistLocalProtocol OBJECT-TYPE  SYNTAX Integer32 (0..255 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The protocol number of the local Endpoint's traffic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.9.
Name: N/A
Description: cipSecEndPtHistLocalPort OBJECT-TYPE  SYNTAX Integer32 (0..65535 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The port number of the local Endpoint's traffic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.10.
Name: N/A
Description: cipSecEndPtHistRemoteName OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The DNS name of the remote Endpoint."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.11.
Name: N/A
Description: cipSecEndPtHistRemoteType OBJECT-TYPE  SYNTAX EndPtType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of identity for the remote Endpoint.  Possible values are:  1) a single IP address, or  2) an IP address range, or  3) an IP subnet."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.3.2.1.12.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.3.2.1.12.1
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.12.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.171.1.4.3.2.1.13.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.171.1.4.3.2.1.13.2
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.13.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.14.
Name: N/A
Description: cipSecEndPtHistRemoteProtocol OBJECT-TYPE  SYNTAX Integer32 (0..255 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The protocol number of the remote Endpoint's traffic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.4.3.2.1.15.
Name: N/A
Description: cipSecEndPtHistRemotePort OBJECT-TYPE  SYNTAX Integer32 (0..65535 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The port number of the remote Endpoint's traffic."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.1.1.1.
Name: cipSecFailTableSize(1)
Description: cipSecFailTableSize OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The window size of the IPsec Phase-1 and Phase-2  Failure Tables.    The IPsec Phase-1 and Phase-2 Failure Tables are  implemented as a sliding window in which only the  last n entries are maintained. This object is used  specify the number of entries which will be  maintained in the IPsec Phase-1 and Phase-2 Failure  Tables.    An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.2.1.1.2.
Name: cikeFailReason(2)
Description: cikeFailReason OBJECT-TYPE  SYNTAX INTEGER {  other(1),  peerDelRequest(2),  peerLost(3),  localFailure(4),  authFailure(5),  hashValidation(6),  encryptFailure(7),  internalError(8),  sysCapExceeded(9),  proposalFailure(10),  peerCertUnavailable(11),  peerCertNotValid(12),  localCertExpired(13),  crlFailure(14),  peerEncodingError(15),  nonExistentSa(16),  operRequest(17)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The reason for the failure. Possible reasons include:  1 = other  2 = peer delete request was received  3 = contact with peer was lost  4 = local failure occurred  5 = authentication failure  6 = hash validation failure  7 = encryption failure  8 = internal error occurred  9 = system capacity failure  10 = proposal failure  11 = peer's certificate is unavailable  12 = peer's certificate was found invalid  13 = local certificate expired  14 = certificate revoke list (crl) failure  15 = peer encoding error  16 = non-existent security association  17 = operator requested termination."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.2.1.1.3.
Name: cikeFailTime(3)
Description: cikeFailTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime in hundredths of seconds  at the time of the failure."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.2.1.1.4.
Name: cikeFailLocalType(4)
Description: cikeFailLocalType OBJECT-TYPE  SYNTAX IkePeerType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of local peer identity. The local peer  may be identified by:  1. an IP address, or  2. a host name."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.2.1.1.5.
Name: cikeFailLocalValue(5)
Description: cikeFailLocalValue OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the local peer identity.    If the local peer type is an IP Address, then this  is the IP Address used to identify the local peer.    If the local peer type is a host name, then this is  the host name used to identify the local peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.2.1.1.6.
Name: cikeFailRemoteType(6)
Description: cikeFailRemoteType OBJECT-TYPE  SYNTAX IkePeerType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of remote peer identity. The remote  peer may be identified by:  1. an IP address, or  2. a host name."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.2.1.1.7.
Name: cikeFailRemoteValue(7)
Description: cikeFailRemoteValue OBJECT-TYPE  SYNTAX DisplayString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the remote peer identity.    If the remote peer type is an IP Address, then this  is the IP Address used to identify the remote peer.    If the remote peer type is a host name, then this is  the host name used to identify the remote peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.2.1.1.8.
Name: cikeFailLocalAddr(8)
Description: cikeFailLocalAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the local peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.2.1.1.9.
Name: cikeFailRemoteAddr(9)
Description: cikeFailRemoteAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the remote peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.3.1.1.2.
Name: cipSecFailReason(2)
Description: cipSecFailReason OBJECT-TYPE  SYNTAX INTEGER {  other(1),  internalError(2),  peerEncodingError(3),  proposalFailure(4),  protocolUseFail(5),  nonExistentSa(6),  decryptFailure(7),  encryptFailure(8),  inAuthFailure(9),  outAuthFailure(10),  compression(11),  sysCapExceeded(12),  peerDelRequest(13),  peerLost(14),  seqNumRollOver(15),  operRequest(16)  }  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The reason for the failure. Possible reasons  include:  1 = other  2 = internal error occurred  3 = peer encoding error  4 = proposal failure  5 = protocol use failure  6 = non-existent security association  7 = decryption failure  8 = encryption failure  9 = inbound authentication failure  10 = outbound authentication failure  11 = compression failure  12 = system capacity failure  13 = peer delete request was received  14 = contact with peer was lost  15 = sequence number rolled over  16 = operator requested termination."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.3.1.1.3.
Name: cipSecFailTime(3)
Description: cipSecFailTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of sysUpTime in hundredths of seconds  at the time of the failure."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.3.1.1.4.
Name: cipSecFailTunnelIndex(4)
Description: cipSecFailTunnelIndex OBJECT-TYPE  SYNTAX Integer32 (1..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The Phase-2 Tunnel index (cipSecTunIndex)."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.3.1.1.5.
Name: cipSecFailSaSpi(5)
Description: cipSecFailSaSpi OBJECT-TYPE  SYNTAX Integer32 (0..2147483647 )  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The security association SPI value."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.3.1.1.6.
Name: cipSecFailPktSrcAddr(6)
Description: cipSecFailPktSrcAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The packet's source IP address."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.5.3.1.1.7.
Name: cipSecFailPktDstAddr(7)
Description: cipSecFailPktDstAddr OBJECT-TYPE  SYNTAX IPSIpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The packet's destination IP address."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.1.
Name: N/A
Description: cipSecTrapCntlIkeTunnelStart OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state of  sending the IPsec IKE Phase-1 Tunnel Start TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.2.
Name: N/A
Description: cipSecTrapCntlIkeTunnelStop OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state  of sending the  IPsec IKE Phase-1 Tunnel Stop TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.3.
Name: N/A
Description: cipSecTrapCntlIkeSysFailure OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state  of sending the  IPsec IKE Phase-1 System Failure TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.4.
Name: N/A
Description: cipSecTrapCntlIkeCertCrlFailure OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative  state of sending the  IPsec IKE Phase-1 Certificate/CRL Failure TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.5.
Name: N/A
Description: cipSecTrapCntlIkeProtocolFail OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative  state of sending the  IPsec IKE Phase-1 Protocol Failure TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.6.
Name: cipSecTrapCntlIkeNoSa(6)
Description: cipSecTrapCntlIkeNoSa OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative  state of sending the  IPsec IKE Phase-1 No Security Association TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.7.
Name: N/A
Description: cipSecTrapCntlIpSecTunnelStart OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state  of sending the IPsec  Phase-2 Tunnel Start TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.8.
Name: N/A
Description: cipSecTrapCntlIpSecTunnelStop OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative  state of sending the IPsec  Phase-2 Tunnel Stop TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.9.
Name: N/A
Description: cipSecTrapCntlIpSecSysFailure OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state  of sending the IPsec  Phase-2 System Failure TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.10.
Name: N/A
Description: cipSecTrapCntlIpSecSetUpFailure OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state  of sending the IPsec  Phase-2 Set Up Failure TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.11.
Name: N/A
Description: cipSecTrapCntlIpSecEarlyTunTerm OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state  of sending the IPsec  Phase-2 Early Tunnel Termination TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.12.
Name: N/A
Description: cipSecTrapCntlIpSecProtocolFail OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state  of sending the IPsec  Phase-2 Protocol Failure TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.171.1.6.13.
Name: N/A
Description: cipSecTrapCntlIpSecNoSa OBJECT-TYPE  SYNTAX TrapStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state  of sending the IPsec  Phase-2 No Security Association TRAP"  DEFVAL { disabled }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.1.1.
Name: N/A
Description: crasMaxSessionsSupportable OBJECT-TYPE  SYNTAX Integer32 (0..2147483647)  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum number of remote access sessions  that may be supported on this device.    If the device imposes no arbitrary limit on the  maximum number of sessions, it should return a  value of 0."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.1.2.
Name: N/A
Description: crasMaxUsersSupportable OBJECT-TYPE  SYNTAX Integer32 (0..2147483647)  UNITS "Users"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum number of remote access users  for whom Remote Access sessions may be supported on  this device.  If the device imposes no arbitrary limit on the  maximum number of users, it should return a  value of 0."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.1.3.
Name: N/A
Description: crasMaxGroupsSupportable OBJECT-TYPE  SYNTAX Integer32 (0..2147483647)  UNITS "Groups"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum number of remote access groups  that may be defined on this device. 'Group'  refers to a collection of users grouped together  for administrative convenience.    If the device imposes no arbitrary limit on  the maximum number of groups, it should return  a value of 0."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.1.4.
Name: N/A
Description: crasNumCryptoAccelerators OBJECT-TYPE  SYNTAX Integer32 (0..2147483647)  UNITS "Users"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum number of hardware crypto accelerators  which can be installed on this device to support  remote access sessions. 'cryptoaccelerator' denotes  a hardware/software entity which the managed entity  uses to offload some or all computations pertaining  to cryptographic operations.    If the device imposes no arbitrary limit on the  number of crypto accelerators to support Remote Access  function, it should return a value of 0."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.2.1.
Name: crasGlobalBwUsage(1)
Description: crasGlobalBwUsage OBJECT-TYPE  SYNTAX Gauge32  UNITS "MBytes/second"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The average bandwidth used by all the active  remote access sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.1.
Name: crasNumSessions(1)
Description: crasNumSessions OBJECT-TYPE  SYNTAX Gauge32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of currently active sessions.    A session is a connection terminating on the managed  entity which has been established to provide remote  access connectivity to a user. A session is said to be  'active' if it is ready to carry application traffic  between the user and the managed entity. A session which  is not active is defined to be 'dormant'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.2.
Name: crasNumPrevSessions(2)
Description: crasNumPrevSessions OBJECT-TYPE  SYNTAX Counter32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of remote access sessions which were  previously active but which where since terminated.  Measured since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.3.
Name: crasNumUsers(3)
Description: crasNumUsers OBJECT-TYPE  SYNTAX Gauge32  UNITS "Users"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of users who have active sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.4.
Name: crasNumGroups(4)
Description: crasNumGroups OBJECT-TYPE  SYNTAX Gauge32  UNITS "Groups"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of user groups whose members have  active sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.5.
Name: crasGlobalInPkts(5)
Description: crasGlobalInPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received by all  currently and previously active remote access  sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.6.
Name: crasGlobalOutPkts(6)
Description: crasGlobalOutPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets transmitted by all  currently and previously active remote access  sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.7.
Name: crasGlobalInOctets(7)
Description: crasGlobalInOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received by all currently  and previously active remote access sessions.  This value is accumulated BEFORE determining whether  or not the packet should be decompressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.8.
Name: N/A
Description: crasGlobalInDecompOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of decompressed octets received  by all current and previous remote access sessions.  This value is accumulated AFTER the packet is  decompressed. If compression is not being used,  this value will match the value of crasGlobalInOctets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.9.
Name: crasGlobalOutOctets(9)
Description: crasGlobalOutOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets transmitted by all  currently and previously active remote access  sessions.    This value is accumulated AFTER determining  whether or not the packet should be compressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.10.
Name: N/A
Description: crasGlobalOutUncompOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of uncompressed octets sent  by all current and previous remote access sessions.  This value is accumulated BEFORE the packet is  compressed. If compression is not being used, this  value will match the value of crasGlobalOutOctets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.11.
Name: crasGlobalInDropPkts(11)
Description: crasGlobalInDropPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets which were dropped  during receive processing by all currently and  previously active remote access sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.12.
Name: N/A
Description: crasGlobalOutDropPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets which were  dropped during receive processing by all  currently and previously active remote access  sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.2.
Name: crasGroup(2)
Description: crasGroup OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The name of the user group to which this remote  access session belongs."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.4.
Name: crasAuthenMethod(4)
Description: crasAuthenMethod OBJECT-TYPE  SYNTAX UserAuthenMethod  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The method used to authenticate the user prior to  establishing the session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.5.
Name: crasAuthorMethod(5)
Description: crasAuthorMethod OBJECT-TYPE  SYNTAX UserAuthorMethod  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The method used to authorize the user prior to  establishing the session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.6.
Name: crasSessionDuration(6)
Description: crasSessionDuration OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of seconds elapsed since this session  was established."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.7.
Name: crasLocalAddressType(7)
Description: crasLocalAddressType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in 'crasLocalAddress'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.8.
Name: crasLocalAddress(8)
Description: crasLocalAddress OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address assigned to the client of this session  in the private network assigned by the managed entity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.9.
Name: crasISPAddressType(9)
Description: crasISPAddressType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in 'crasISPAddress'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.10.
Name: crasISPAddress(10)
Description: crasISPAddress OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the peer (client) assigned by the ISP.  This is the address of the client device in the public  network."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.11.
Name: crasSessionProtocol(11)
Description: crasSessionProtocol OBJECT-TYPE  SYNTAX RasProtocol  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The protocol underlying this remote access session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.12.
Name: crasProtocolElement(12)
Description: crasProtocolElement OBJECT-TYPE  SYNTAX OBJECT IDENTIFIER  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "A reference to MIB definitions specific to the protocol  underlying corresponding to the session or tunnel  used to realized the remote access session corresponding  to this conceptual row.  For instance, if this remote access session is based on  IPsec, then this object must contain the complete  instance identifier of the IPsec tunnel corresponding  to this remote access session.  If no MIB definitions specific to the underlying  protocol are available, the value should be set to the  OBJECT IDENTIFIER {0 0}."  DEFVAL {zeroDotZero}
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.13.
Name: N/A
Description: crasSessionEncryptionAlgo OBJECT-TYPE  SYNTAX SessionEncrAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The algorithm used by this remote access session to  encrypt its payload."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.14.
Name: N/A
Description: crasSessionPktAuthenAlgo OBJECT-TYPE  SYNTAX SessionAuthAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The algorithm used by this remote access session to  to validate packets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.15.
Name: N/A
Description: crasSessionCompressionAlgo OBJECT-TYPE  SYNTAX SessionCompressionAlgo  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The algorithm used by this remote access session to  compress packets."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.16.
Name: N/A
Description: crasHeartbeatInterval OBJECT-TYPE  SYNTAX Unsigned32 (0..4294967295)  UNITS "Seconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The interval in seconds between two successive heartbeats  employed by this session. Value of 0 denotes that no  heartbeat is used."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.17.
Name: N/A
Description: crasClientVendorString OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The string identifying the vendor of the client  application initiating this Remote Access session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.18.
Name: N/A
Description: crasClientVersionString OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The string identifying the version of the of the client  application initiating the Remote Access session.  This can be used by the administrator to identify which  users are running unsupported client versions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.19.
Name: N/A
Description: crasClientOSVendorString OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The string identifying the vendor of the operating system  on which the client application initiating the Remote Access  Session is running."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.20.
Name: N/A
Description: crasClientOSVersionString OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The string identifying the version of the operating  system of the entity which initiated this Remote Access  session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.21.
Name: N/A
Description: crasPrimWINSServerAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in  'crasPrimWINSServer'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.22.
Name: crasPrimWINSServer(22)
Description: crasPrimWINSServer OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the primary WINS server assigned  managed entity to this client session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.23.
Name: N/A
Description: crasSecWINSServerAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in  'crasSecWINSServer'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.24.
Name: crasSecWINSServer(24)
Description: crasSecWINSServer OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the secondary WINS server assigned  by the managed entity to this client session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.25.
Name: N/A
Description: crasPrimDNSServerAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in  'crasPrimDNSServer'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.26.
Name: crasPrimDNSServer(26)
Description: crasPrimDNSServer OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the primary DNS server assigned by  the managed entity to this client session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.27.
Name: N/A
Description: crasSecDNSServerAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in  'crasSecDNSServer'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.28.
Name: crasSecDNSServer(28)
Description: crasSecDNSServer OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the secondary DNS server assigned  by the managed entity to this client session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.29.
Name: N/A
Description: crasDHCPServerAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in  'crasDHCPServer'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.30.
Name: crasDHCPServer(30)
Description: crasDHCPServer OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The IP address of the DHCP server assigned by the  managed entity to this client session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.31.
Name: crasSessionInPkts(31)
Description: crasSessionInPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received by this Remote  Access session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.32.
Name: crasSessionOutPkts(32)
Description: crasSessionOutPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets transmitted by this  Remote Access Session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.33.
Name: N/A
Description: crasSessionInDropPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received for processing  on this session which were dropped by the managed entity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.34.
Name: N/A
Description: crasSessionOutDropPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outgoing packets on this session  which were dropped during transmit processing by the  managed entity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.35.
Name: crasSessionInOctets(35)
Description: crasSessionInOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received by this Remote  Access Session.    This value is accumulated BEFORE determining whether  or not the packet should be decompressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.36.
Name: crasSessionOutOctets(36)
Description: crasSessionOutOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets transmitted by this Remote  Access Session.    This value is accumulated AFTER determining whether  or not the packet should be compressed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.21.1.37.
Name: crasSessionState(37)
Description: crasSessionState OBJECT-TYPE  SYNTAX SessionStatus  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The state of the remote access session corresponding  to this conceptual row.    The management entity may use this object to terminate  an established session by setting value of the object  to 'terminating'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.22.1.2.
Name: crasActGrNumUsers(2)
Description: crasActGrNumUsers OBJECT-TYPE  SYNTAX Integer32 (1..2147483647)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of users in this group currently connected  to the managed device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.22.1.3.
Name: crasActGrpInPkts(3)
Description: crasActGrpInPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets received by this session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.22.1.4.
Name: crasActGrpOutPkts(4)
Description: crasActGrpOutPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets transmitted by this session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.22.1.5.
Name: crasActGrpInDropPkts(5)
Description: crasActGrpInDropPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets dropped by this session  which were received for processing."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.22.1.6.
Name: crasActGrpOutDropPkts(6)
Description: crasActGrpOutDropPkts OBJECT-TYPE  SYNTAX Counter64  UNITS "Packets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of outgoing packets which were  dropped during transmit processing by this session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.22.1.7.
Name: crasActGrpInOctets(7)
Description: crasActGrpInOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets received by this session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.22.1.8.
Name: crasActGrpOutOctets(8)
Description: crasActGrpOutOctets OBJECT-TYPE  SYNTAX Counter64  UNITS "Octets"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets transmitted by this session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.23.
Name: crasEmailNumSessions(23)
Description: crasEmailNumSessions OBJECT-TYPE  SYNTAX Gauge32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of currently active Email proxy sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.24.
Name: N/A
Description: crasEmailCumulateSessions OBJECT-TYPE  SYNTAX Counter32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of cumulative Email proxy sessions since system up."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.25.
Name: N/A
Description: crasEmailPeakConcurrentSessions OBJECT-TYPE  SYNTAX Unsigned32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of peak concurrent Email proxy sessions since system up."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.26.
Name: crasIPSecNumSessions(26)
Description: crasIPSecNumSessions OBJECT-TYPE  SYNTAX Gauge32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of currently active IPSec sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.27.
Name: N/A
Description: crasIPSecCumulateSessions OBJECT-TYPE  SYNTAX Counter32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of cumulative IPSec sessions since system up."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.392.1.3.28.: HTTPSConnectionPool(host='oid-base.com', port=443): Max retries exceeded with url: /get/1.3.6.1.4.1.9.9.392.1.3.28. (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x790bdfd6cce0>: Failed to establish a new connection: [Errno 101] Network is unreachable'))
OID: 1.3.6.1.4.1.9.9.392.1.3.28.
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.392.1.3.29.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.392.1.3.29.2
OID: 1.3.6.1.4.1.9.9.392.1.3.29.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.392.1.3.30.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.392.1.3.30.2
OID: 1.3.6.1.4.1.9.9.392.1.3.30.2
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.392.1.3.31.2: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.392.1.3.31.2
OID: 1.3.6.1.4.1.9.9.392.1.3.31.2
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.32.
Name: crasLBNumSessions(32)
Description: crasLBNumSessions OBJECT-TYPE  SYNTAX Gauge32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of currently active Load Balancing sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.33.
Name: N/A
Description: crasLBCumulateSessions OBJECT-TYPE  SYNTAX Counter32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of cumulative Load Balancing sessions since system up."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.34.
Name: N/A
Description: crasLBPeakConcurrentSessions OBJECT-TYPE  SYNTAX Unsigned32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of peak concurrent Load Balancing sessions since system up."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.35.
Name: crasSVCNumSessions(35)
Description: crasSVCNumSessions OBJECT-TYPE  SYNTAX Gauge32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of currently active SVC sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.36.
Name: N/A
Description: crasSVCCumulateSessions OBJECT-TYPE  SYNTAX Counter32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of cumulative SVC sessions since system up."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.37.
Name: N/A
Description: crasSVCPeakConcurrentSessions OBJECT-TYPE  SYNTAX Unsigned32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of peak concurrent SVC sessions since system up."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.38.
Name: N/A
Description: crasWebvpnNumSessions OBJECT-TYPE  SYNTAX Gauge32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of currently active Webvpn sessions."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.39.
Name: N/A
Description: crasWebvpnCumulateSessions OBJECT-TYPE  SYNTAX Counter32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of cumulative Webvpn sessions since system up."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.3.40.
Name: N/A
Description: crasWebvpnPeakConcurrentSessions OBJECT-TYPE  SYNTAX Unsigned32  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of peak concurrent Webvpn sessions since system up."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.1.1.
Name: crasNumTotalFailures(1)
Description: crasNumTotalFailures OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of attempts to establish sessions which  failed, since the last reboot of the managed device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.1.2.
Name: N/A
Description: crasNumDeclinedSessions OBJECT-TYPE  SYNTAX Unsigned32 (0..4294967295)  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of session setup attempts, counted since  the last time the notification  'ciscoRasTooManyFailedAuths' was issued, which were  declined due to authentication or authorization  failure."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.1.3.
Name: N/A
Description: crasNumSetupFailInsufResources OBJECT-TYPE  SYNTAX Counter64  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of session setup attempts that failed  due to insufficient resources."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.1.4.
Name: N/A
Description: crasNumAbortedSessions OBJECT-TYPE  SYNTAX Counter64  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of sessions which were successfully  setup but were since terminated abnormally."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.2.1.
Name: crasFailTableSize(1)
Description: crasFailTableSize OBJECT-TYPE  SYNTAX Unsigned32 (0..4294967295)  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "The window size of the Remote Access Failure tables.    The failure tables for session and group failures  maintain only the last crasFailTableSize number of  failure records. A value of 0 for this MIB variable  indicates that archiving of the failures is disabled.    An implementation may choose suitable minimum and  maximum values for this element based on the local  policy and available resources. If an SNMP SET request  specifies a value outside this window for this element,  a BAD VALUE may be returned."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.2.
Name: crasSessFailUsername(2)
Description: crasSessFailUsername OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The name of the user associated with this failed  remote access session."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.3.
Name: crasSessFailGroupname(3)
Description: crasSessFailGroupname OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The name of the user group to which this failed  remote access session belongs."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.4.
Name: crasSessFailType(4)
Description: crasSessFailType OBJECT-TYPE  SYNTAX INTEGER {setupFailure(1), operationalFailure(2)}  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the failure:  1 = failure occurred during session setup  2 = failed occurred after the session was setup  successfully."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.5.
Name: crasSessFailReason(5)
Description: crasSessFailReason OBJECT-TYPE  SYNTAX INTEGER {other(1), internalError(2), authenticationFailure(3), authorizationFailure(4), sysCapExceeded(5), peerAbortRequest(6), peerLost(7), operRequest(8)}  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The reason for the failure. Possible reasons  include:  1 = other (error which cannot be classified in  any of the types listed below).  2 = internal error occurred  3 = failed to authenticate the peer/user  4 = failed to authorize the peer/user  5 = system capacity exceeded (memory, cpu, max  users etc)  6 = peer requested to abort the session or the  setup  7 = lost peer's heartbeat  8 = local management request."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.6.
Name: crasSessFailTime(6)
Description: crasSessFailTime OBJECT-TYPE  SYNTAX TimeStamp  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of the MIB element 'sysUpTime'  at the time of the failure."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.7.
Name: N/A
Description: crasSessFailSessionIndex OBJECT-TYPE  SYNTAX SessionIndex  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The index of the session which failed (in case  this was an operational failure). In case of setup  failures (where the value of 'crasSessFailType' of  this conceptual row is 'operationalFailure'), the  value of this object is undefined and should not be  processed."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.8.
Name: N/A
Description: crasSessFailISPAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in  'crasSessFailISPAddr'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.9.
Name: crasSessFailISPAddr(9)
Description: crasSessFailISPAddr OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The public address of the peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.10.
Name: N/A
Description: crasSessFailLocalAddrType OBJECT-TYPE  SYNTAX InetAddressType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the address returned in  'crasSessFailLocalAddr'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.1.1.11.
Name: N/A
Description: crasSessFailLocalAddr OBJECT-TYPE  SYNTAX InetAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The address assigned to the peer by the local  address management mechanism. In case no address  was assigned to the peer when the failure occurred,  this MIB variable would contain the IPv4 address  value 0.0.0.0"
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.3.2.
Name: crasFailLastFailIndex(2)
Description: crasFailLastFailIndex OBJECT-TYPE  SYNTAX FailureRecordIndex  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of column 'crasSessFailIndex'  corresponding to the last row added to the  crasSessFailTable.    The value of this object is undefined and should  not be processed by the management entity if the  value of the object 'crasFailTableSize' is 0."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.4.1.1.2.
Name: N/A
Description: crasGrpFailNumFailAuths OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of sessions belonging to this group which  failed authentication; counted since last reboot."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.4.1.1.3.
Name: N/A
Description: crasGrpFailNumResourceFailures OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of session setup attempts which failed due  to insufficient resources."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.4.1.1.4.
Name: N/A
Description: crasGrpFailNumDeclined OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of session setup attempts which were declined  by the managed entity due to local policy. These would  include sessions which were denied due to rate control  settings."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.4.1.1.5.
Name: N/A
Description: crasGrpFailNumTerminatedMgmt OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of established sessions which were terminated  by explicit management action. The termination may have  been triggered locally or based on a request from the peer."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.4.4.1.1.6.
Name: N/A
Description: crasGrpFailNumTerminatedOther OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of established sessions which were  terminated due to insufficient reasons, internal error  or other reasons not caused by management action."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.5.1.1.
Name: N/A
Description: crasNumDisabledAccounts OBJECT-TYPE  SYNTAX Counter64  UNITS "Users"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of user accounts which were  disabled due to repeated login failures."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.6.1.
Name: crasThrMaxSessions(1)
Description: crasThrMaxSessions OBJECT-TYPE  SYNTAX Integer32 (0..2147483647)  UNITS "Sessions"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum number of sessions which are successfully  setup after which the managed entity should alert the  network management entity using the notification  'ciscoRasTooManySessions', if the notification has been  enabled.  A value of 0 indicates that the threshold has not been  set."  DEFVAL {0}
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.6.2.
Name: crasThrMaxFailedAuths(2)
Description: crasThrMaxFailedAuths OBJECT-TYPE  SYNTAX Unsigned32 (0..4294967295)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of object 'crasNumDeclinedSessions' at  which the managed entity should alert the network  management entity using the notification  'ciscoRasTooManyFailedAuths', if the notification  has been enabled.  A value of 0 indicates that the threshold has not been  set."  DEFVAL {4294967295}
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.6.3.
Name: crasThrMaxThroughput(3)
Description: crasThrMaxThroughput OBJECT-TYPE  SYNTAX Integer32 (0..2147483647)  UNITS "Octets Per Second"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The highest throughput of the Remote Access Service at  which the managed entity should alert the network management  entity using the notification 'ciscoRasTooHighThroughput',  if the notification has been enabled.  The notification is disabled till the value of the  aggregate throughput of the managed entity drops below  the value of this object.  A value of 0 indicates that the threshold has not been  set."  DEFVAL {0}
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.7.1.
Name: N/A
Description: crasCntlTooManySessions OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state of  sending the trap to signal the violation of the  Max session threshold."  DEFVAL { false }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.7.2.
Name: N/A
Description: crasCntlTooManyFailedAuths OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state of  sending the trap to signal the violation of the  Max authentication failure count threshold."  DEFVAL { false }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.392.1.7.3.
Name: N/A
Description: crasCntlTooHighThroughput OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This object defines the administrative state of  sending the trap to signal the violation of the  Max throughput threshold."  DEFVAL { false }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.1.1.
Name: ccaSupportsHwCrypto(1)
Description: ccaSupportsHwCrypto OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This MIB object assumes the value of True if the  managed device is capable of including hardware crypto  accelerator."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.1.2.
Name: N/A
Description: ccaSupportsModularHwCrypto OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "This MIB object assumes the value of True if the  managed device supports field removable hardware  crypto accelerators."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.1.3.
Name: ccaMaxAccelerators(3)
Description: ccaMaxAccelerators OBJECT-TYPE  SYNTAX Integer32 (-1..50)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum number of hardware crypto accelerators  which may be simultaneously operational in this device.  If the managed device can support only software  encryption, the value of this MIB object should be set  to zero.  If there is not set limit on the maximum number of  crypto accelerator modules which the managed device  can support, the agent should return a value of '-1'  for this MIB variable."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.1.4.
Name: N/A
Description: ccaMaxCryptoThroughput OBJECT-TYPE  SYNTAX Unsigned32  UNITS "megabits per second"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum crypto throughput that may be supported  by the managed device with the current number of active  crypto accelerators.  If this value cannot be determined, the agent should  return a value of 0."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.1.5.
Name: N/A
Description: ccaMaxCryptoConnections OBJECT-TYPE  SYNTAX Unsigned32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum number of VPN flows (connections) the managed  device can support with the current number of active  crypto accelerators.  If this value cannot be determined, the agent should  return a value of 0."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.1.1.
Name: N/A
Description: ccaGlobalNumActiveAccelerators OBJECT-TYPE  SYNTAX CAModuleCount  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of crypto accelerators which are in state  'active'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.1.2.
Name: N/A
Description: ccaGlobalNumNonOperAccelerators OBJECT-TYPE  SYNTAX CAModuleCount  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of crypto accelerators which are in a state  other than 'active'."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.1.3.
Name: ccaGlobalInOctets(3)
Description: ccaGlobalInOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets input to all the crypto  accelerators installed in the device.  The value is cumulative from last reboot of the  managed entity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.1.4.
Name: ccaGlobalOutOctets(4)
Description: ccaGlobalOutOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of octets output by all the crypto  accelerators installed in the device.  The value is cumulative from last reboot of the  managed entity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.1.5.
Name: ccaGlobalInPkts(5)
Description: ccaGlobalInPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets input to all the crypto  accelerators installed in the device.  The value is cumulative from last reboot of the  managed entity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.1.6.
Name: ccaGlobalOutPkts(6)
Description: ccaGlobalOutPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets output by all the crypto  accelerators installed in the device.  The value is cumulative from last reboot of the  managed entity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.1.7.
Name: ccaGlobalOutErrPkts(7)
Description: ccaGlobalOutErrPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The total number of packets output by all the crypto  accelerators installed in the device which were found  to be generated with errors (checksum errors, other  errors).  The value is cumulative from last reboot of the  managed entity."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.2.
Name: N/A
Description: ccaAcclEntPhysicalIndex OBJECT-TYPE  SYNTAX EntPhysicalIndexOrZero  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The value of entPhysicalIndex of the module  corresponding to this conceptual row or zero,  if the module is not an entity listed in  'entPhysicalTable' of rfc2737."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.3.
Name: ccaAcclStatus(3)
Description: ccaAcclStatus OBJECT-TYPE  SYNTAX ModuleOperType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The state of the crypto accelerator corresponding  to this row."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.4.
Name: ccaAcclType(4)
Description: ccaAcclType OBJECT-TYPE  SYNTAX CAModuleType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The type of the crypto accelerator corresponding to  this row."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.5.
Name: ccaAcclVersion(5)
Description: ccaAcclVersion OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The version string of the firmware of the crypto  accelerator corresponding to this row."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.6.
Name: ccaAcclSlot(6)
Description: ccaAcclSlot OBJECT-TYPE  SYNTAX Unsigned32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The slot number of the crypto accelerator  corresponding to this row."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.7.
Name: ccaAcclActiveTime(7)
Description: ccaAcclActiveTime OBJECT-TYPE  SYNTAX TimeTicks  UNITS "seconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of seconds elapsed since the crypto  accelerator corresponding to this row transitioned  into the 'active' state."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.8.
Name: ccaAcclInPkts(8)
Description: ccaAcclInPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets input to this module for  processing since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.9.
Name: ccaAcclOutPkts(9)
Description: ccaAcclOutPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets output by this module after  processing, since last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.10.
Name: ccaAcclOutBadPkts(10)
Description: ccaAcclOutBadPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets output by this module after  processing which had crypto errors, since last reboot  of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.11.
Name: ccaAcclInOctets(11)
Description: ccaAcclInOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets input to this module for  processing since last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.12.
Name: ccaAcclOutOctets(12)
Description: ccaAcclOutOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets output by this module after  processing since last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.13.
Name: N/A
Description: ccaAcclHashOutboundPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets output by this module which  were prepared for hash validation since the last  reboot of the device.  Hash validation is a cryptographic operation used  to verify the integrity of a block of data received  from a trusted source."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.14.
Name: N/A
Description: ccaAcclHashOutboundOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets output by this module which were  prepared for hash validation since the last reboot of  the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.15.
Name: N/A
Description: ccaAcclHashInboundPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets input to this module which  required hash validation since the last reboot of  the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.16.
Name: N/A
Description: ccaAcclHashInboundOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets input to this module which were  authenticated using hash validation since the last  reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.17.
Name: ccaAcclEncryptPkts(17)
Description: ccaAcclEncryptPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets input to this module which  required encryption since the last reboot of the  device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.18.
Name: ccaAcclEncryptOctets(18)
Description: ccaAcclEncryptOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets input to this module which  required encryption since the last reboot of the  device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.19.
Name: ccaAcclDecryptPkts(19)
Description: ccaAcclDecryptPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets input to this module which  required decryption since the last reboot of the  device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.20.
Name: ccaAcclDecryptOctets(20)
Description: ccaAcclDecryptOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets input to this module which  required decryption since the last reboot of the  device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.21.
Name: N/A
Description: ccaAcclTransformsTotal OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of cryptographic transformations performed  by this crypto accelerator since the last reboot of the  device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.22.
Name: ccaAcclDropsPkts(22)
Description: ccaAcclDropsPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets input to this module which were  dropped prior to processing since the last reboot of  the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.23.
Name: ccaAcclRandRequests(23)
Description: ccaAcclRandRequests OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of requests received by this crypto  accelerator to generate random numbers since the last  reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.24.
Name: ccaAcclRandReqFails(24)
Description: ccaAcclRandReqFails OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of random number requests received by this  module which were not fulfilled, counted since the last  reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.25.
Name: N/A
Description: ccaAcclDHKeysGenerated OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of Diffie Hellman key pairs generated by  this module since the last reboot."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.26.
Name: N/A
Description: ccaAcclDHDerivedSecretKeys OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times this module has derived Diffie Hellman  secret keys since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.27.
Name: N/A
Description: ccaAcclRSAKeysGenerated OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times a new RSA key pair was generated  by this module, counted since the last time this module  assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.28.
Name: ccaAcclRSASignings(28)
Description: ccaAcclRSASignings OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times an RSA Digital Signature has been  generated by this module, counted since the last time  this module assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.29.
Name: N/A
Description: ccaAcclRSAVerifications OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times an RSA Digital Signature has  been verified by this module, counted since the last  time this module assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.30.
Name: N/A
Description: ccaAcclRSAEncryptPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets input to this module which  required RSA encryption, counted since the last time  this module assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.31.
Name: N/A
Description: ccaAcclRSAEncryptOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets input to this module which  required RSA encryption, counted since the last time  this module assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.32.
Name: N/A
Description: ccaAcclRSADecryptPkts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of packets input to this module which  required RSA decryption, counted since the last time  this module assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.33.
Name: N/A
Description: ccaAcclRSADecryptOctets OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets input to this module which  required RSA decryption, counted since the last time  this module assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.34.
Name: N/A
Description: ccaAcclDSAKeysGenerated OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times DSA key pair has been generated by  this module, counted since the last time this module  assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.35.
Name: ccaAcclDSASignings(35)
Description: ccaAcclDSASignings OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times DSA signature has been generated  by this module, counted since the last time this module  assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.36.
Name: N/A
Description: ccaAcclDSAVerifications OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times DSA signature has been verified  by this module, counted since the last time this module  assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.37.
Name: N/A
Description: ccaAcclOutboundSSLRecords OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of combined outbound hash/encrypt SSL  records processed by this module, counted since the  last time this module assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.2.1.38.
Name: N/A
Description: ccaAcclInboundSSLRecords OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of combined inbound hash/encrypt SSL  records processed by this module, counted since the  last time this module assumed 'active' status."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.2.
Name: N/A
Description: ccaProtPktEncryptsReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of payload encrypt requests received by  the crypto accelerators from this security protocol,  counted since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.3.
Name: N/A
Description: ccaProtPktDecryptsReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of payload decrypt requests received by  the crypto accelerators from this security protocol,  counted since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.4.
Name: ccaProtHmacCalcReqs(4)
Description: ccaProtHmacCalcReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times keyed HMAC calculation requests  were received by the crypto accelerators due to the  operation of this security protocol, counted since  the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.5.
Name: ccaProtSaCreateReqs(5)
Description: ccaProtSaCreateReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times requests for creation of  security associations were received by the crypto  accelerators from this security protocol, counted  since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.6.
Name: ccaProtSaRekeyReqs(6)
Description: ccaProtSaRekeyReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times requests for rekeying of  existing security associations were received by  the crypto accelerators from this security protocol,  counted since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.7.
Name: ccaProtSaDeleteReqs(7)
Description: ccaProtSaDeleteReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times requests for deletion of  security associations were received by the crypto  accelerators from this security protocol, counted  since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.8.
Name: ccaProtPktEncapReqs(8)
Description: ccaProtPktEncapReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times requests for payload  encapsulation were received by the crypto accelerators  from this security protocol, counted since the last  reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.9.
Name: ccaProtPktDecapReqs(9)
Description: ccaProtPktDecapReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times requests for payload decapsulation  were received by the crypto accelerators from this  security protocol, counted since the last reboot of  the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.10.
Name: N/A
Description: ccaProtNextPhaseKeyAllocReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times requests for allocation of  keys for the next phase of the protocol operation  which were received by the crypto accelerators from  this security protocol, counted since the last reboot  of the device.  As an example, for IKE, this would identify the number  of times key allocation requests for Quick Mode were  received by the crypto accelerator from the IKE protocol  engine."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.11.
Name: ccaProtRndGenReqs(11)
Description: ccaProtRndGenReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times requests for generation of  random number(s) were received by the crypto  accelerators from this security protocol, counted  since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.2.3.1.1.12.
Name: ccaProtFailedReqs(12)
Description: ccaProtFailedReqs OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times requests received from this  security protocol could not be fulfilled, counted  since the last reboot of the device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.3.1.
Name: N/A
Description: ccaNotifCntlAcclInserted OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This variable controls the generation of  'ciscoCryAccelInserted' notification.  When this variable is set to 'true', generation  of the notification is enabled. When this variable  is set to 'false', generation of the notification  is disabled."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.3.2.
Name: N/A
Description: ccaNotifCntlAcclRemoved OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This variable controls the generation of  'ciscoCryAccelRemoved' notification.  When this variable is set to 'true', generation of  the notification is enabled. When this variable is  set to 'false', generation of the notification is  disabled."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.3.3.
Name: N/A
Description: ccaNotifCntlAcclOperational OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This variable controls the generation of  'ciscoCryAccelOperational' notification.  When this variable is set to 'true', generation  of the notification is enabled. When this variable  is set to 'false', generation of the notification  is disabled."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.467.1.3.4.
Name: N/A
Description: ccaNotifCntlAcclDisabled OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-write  STATUS current  DESCRIPTION  "This variable controls the generation of  'ciscoCryAccelDisabled' notification.  When this variable is set to 'true', generation of  the notification is enabled. When this variable is  set to 'false', generation of the notification is  disabled."  DEFVAL { false }
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.1.1.4.
Name: N/A
Description: cufwConnGlobalNumResDeclined OBJECT-TYPE  SYNTAX Counter64  UNITS "Connections"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of connections which were attempted to  be setup but which were declined due to  non-availability of required resources.  This value is accumulated from the last reboot of  the firewall."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.1.1.6.
Name: N/A
Description: cufwConnGlobalNumActive OBJECT-TYPE  SYNTAX Gauge32  UNITS "Connections"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of connections which are currently active."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.1.1.10.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.1.1.10.1
OID: 1.3.6.1.4.1.9.9.491.1.1.1.10.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.1.1.11.5: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.1.1.11.5
OID: 1.3.6.1.4.1.9.9.491.1.1.1.11.5
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.1.4.1.1.9.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.1.4.1.1.9.1
OID: 1.3.6.1.4.1.9.9.491.1.1.4.1.1.9.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.1.4.1.1.10.5: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.1.4.1.1.10.5
OID: 1.3.6.1.4.1.9.9.491.1.1.4.1.1.10.5
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.1.2.
Name: N/A
Description: cufwUrlfRequestsNumProcessed OBJECT-TYPE  SYNTAX Counter64  UNITS "Requests"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access requests processed by  this firewall.  This value is accumulated from the last reboot of  the firewall."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.3.1.3.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.3.1.3.1
OID: 1.3.6.1.4.1.9.9.491.1.3.1.3.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.3.1.4.5: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.3.1.4.5
OID: 1.3.6.1.4.1.9.9.491.1.3.1.4.5
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.1.5.
Name: N/A
Description: cufwUrlfRequestsNumAllowed OBJECT-TYPE  SYNTAX Counter64  UNITS "Requests"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access requests allowed by  this firewall, due to a directive from a URL  filtering server or a static policy configured on  the firewall.  This value is accumulated from the last reboot of the  firewall."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.1.6.
Name: N/A
Description: cufwUrlfRequestsNumDenied OBJECT-TYPE  SYNTAX Counter64  UNITS "Requests"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access requests declined by  this firewall, due to a directive from a URL  filtering server, a static policy configured on  the firewall, due to resource constraints or  any other reason.  This value is accumulated from the last reboot of  the firewall."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.3.1.7.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.3.1.7.1
OID: 1.3.6.1.4.1.9.9.491.1.3.1.7.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.3.1.8.5: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.3.1.8.5
OID: 1.3.6.1.4.1.9.9.491.1.3.1.8.5
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.1.9.
Name: N/A
Description: cufwUrlfRequestsNumCacheAllowed OBJECT-TYPE  SYNTAX Counter64  UNITS "Requests"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access requests allowed by  the firewall because of a cached entry holding the  result from a previous URL access request that was  handled either by a URLF Server or exclusive domain  configuration.  This value is accumulated from the last reboot of the  firewall."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.1.10.
Name: N/A
Description: cufwUrlfRequestsNumCacheDenied OBJECT-TYPE  SYNTAX Counter64  UNITS "Requests"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access requests denied by  the firewall because of a cached entry holding the  result from a previous URL access request that was  handled either by a URLF Server or exclusive domain  configuration.  This value is accumulated from the last reboot of the  firewall."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.1.13.
Name: N/A
Description: cufwUrlfRequestsNumResDropped OBJECT-TYPE  SYNTAX Counter64  UNITS "Requests"  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of incoming URL access requests that  were dropped by the firewall because of resource  constraints.  This value is accumulated from the last reboot of the  firewall."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.3.1.14.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.3.1.14.1
OID: 1.3.6.1.4.1.9.9.491.1.3.1.14.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.3.1.15.5: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.3.1.15.5
OID: 1.3.6.1.4.1.9.9.491.1.3.1.15.5
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.1.16.
Name: N/A
Description: cufwUrlfNumServerTimeouts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the firewall failed to receive  a response from the configured URL filtering servers  for a request to authorize a URL access request.  This is equal to the number of times a firewall removed  a URL access request from the queue of pending requests  because no response was received from the URL filtering  server(s).  This value is accumulated from the last reboot of the  firewall."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.1.17.
Name: N/A
Description: cufwUrlfNumServerRetries OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access authorization requests  re-sent by the firewall to the URL Filtering Servers  because a response was not received within the  configured time interval.  This value is accumulated from the last reboot of the  firewall."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.4.
Name: cufwUrlfServerVendor(4)
Description: cufwUrlfServerVendor OBJECT-TYPE  SYNTAX CFWUrlfVendorId  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The vendor type of the URL filtering server."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.5.
Name: cufwUrlfServerStatus(5)
Description: cufwUrlfServerStatus OBJECT-TYPE  SYNTAX CFWUrlServerStatus  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The status of the URL filtering server  corresponding to this conceptual row."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.6.
Name: N/A
Description: cufwUrlfServerReqsNumProcessed OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access requests forwarded by  the managed firewall device to the URL filtering  server corresponding to this conceptual row.  This value is counted from the last reboot of  the managed device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.7.
Name: N/A
Description: cufwUrlfServerReqsNumAllowed OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access requests allowed by the  URL filtering server corresponding to this conceptual  row. This counter does not include late responses.  This value is counted from the last reboot of  the managed device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.8.
Name: N/A
Description: cufwUrlfServerReqsNumDenied OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access requests denied by the  URL filtering server corresponding to this conceptual  row. This counter does not include late responses.  This value is counted from the last reboot of  the managed device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.9.
Name: N/A
Description: cufwUrlfServerNumTimeouts OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of times the firewall failed to receive  a response from the URL filtering server corresponding  to this conceptual row, for a request to authorize a  URL access request.  This is equal to the number of times a firewall removed  a URL access request from the queue of pending requests  because no response was received from the URL filtering  server.  This value is accumulated from the last reboot of the  firewall."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.10.
Name: N/A
Description: cufwUrlfServerNumRetries OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access authorization requests  re-sent by the firewall to the URL Filtering Server  corresponding to this conceptual row, because a response  was not received within the configured time interval  from the server.  This value is counted from the last reboot of  the managed device."
----------------------------------------
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.11.
Name: N/A
Description: cufwUrlfServerRespsNumReceived OBJECT-TYPE  SYNTAX Counter64  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of URL access responses received by the  firewall from the URL filtering server corresponding  to this conceptual row. This counter does not include  late responses.  This value is counted from the last reboot of  the managed device."
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.3.3.1.1.13.1: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.3.3.1.1.13.1
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.13.1
Name: N/A
Description: N/A
----------------------------------------
Error fetching OID 1.3.6.1.4.1.9.9.491.1.3.3.1.1.14.5: 404 Client Error: Not Found for url: https://oid-base.com/get/1.3.6.1.4.1.9.9.491.1.3.3.1.1.14.5
OID: 1.3.6.1.4.1.9.9.491.1.3.3.1.1.14.5
Name: N/A
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.10.135.1.1.1.3.
Name: crasVpnUsername(3)
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.10.135.1.1.1.4.
Name: crasVpnUserVlanId(4)
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.9.10.135.1.1.1.5.
Name: crasVpnVlanType(5)
Description: N/A
----------------------------------------
OID: 1.3.6.1.4.1.99.12.35.1.1.1.
Name: usmTargetTagEntry(1)
Description: usmTargetTagEntry OBJECT-TYPE  SYNTAX UsmTargetTagEntry  MAX-ACCESS not-accessible  STATUS current  DESCRIPTION  "Adds an SnmpTagValue to a usmUserEntry."  AUGMENTS { usmUserEntry }
----------------------------------------
OID: 1.3.6.1.4.1.99.12.36.1.1.1.
Name: tgtAddressMaskEntry(1)
Description: tgtAddressMaskEntry OBJECT-TYPE  SYNTAX TgtAddressMaskEntry  MAX-ACCESS not-accessible  STATUS current  DESCRIPTION  "Adds an address mask to an snmpTargetAddrEntry."  AUGMENTS { snmpTargetAddrEntry }
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.26.1.1.
Name: N/A
Description: alSslStatsTotalSessions OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of total sessions."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.26.1.2.
Name: N/A
Description: alSslStatsActiveSessions OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The current number of active sessions."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.26.1.3.
Name: alSslStatsMaxSessions(3)
Description: alSslStatsMaxSessions OBJECT-TYPE  SYNTAX Gauge32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The maximum number current of active sessions at  any one time."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.26.1.4.
Name: N/A
Description: alSslStatsPreDecryptOctets OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets sent to the decryption engine. Includes  octets used as part of negotiation."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.26.1.5.
Name: N/A
Description: alSslStatsPostDecryptOctets OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets received from the decryption engine."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.26.1.6.
Name: N/A
Description: alSslStatsPreEncryptOctets OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets send to the encryption engine."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.26.1.7.
Name: N/A
Description: alSslStatsPostEncryptOctets OBJECT-TYPE  SYNTAX Counter32  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of octets received from the encryption engine.  Includes octets used as part of negitiation."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.1.1.
Name: alLBSSFRole(1)
Description: alLBSSFRole OBJECT-TYPE  SYNTAX DeviceRole  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The role of this device."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.1.2.
Name: alLBSSFDeviceType(2)
Description: alLBSSFDeviceType OBJECT-TYPE  SYNTAX DeviceType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Device type of this device."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.1.3.
Name: alLBSSFActive(3)
Description: alLBSSFActive OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates if device is active or not."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.1.4.
Name: alLBSSFNumberOfPeers(4)
Description: alLBSSFNumberOfPeers OBJECT-TYPE  SYNTAX Gauge32 (0..25)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The number of total current peers."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.1.5.
Name: alLBSSFLoad(5)
Description: alLBSSFLoad OBJECT-TYPE  SYNTAX Gauge32 (0..100)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The current calculated load of this device in percentage."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.1.
Name: alLBSSFPeerRowStatus(1)
Description: alLBSSFPeerRowStatus OBJECT-TYPE  SYNTAX RowStatus  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The status of this row."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.2.
Name: N/A
Description: alLBSSFPeerPrivIpAddress OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Private LAN Ip address of this peer entry."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.3.
Name: N/A
Description: alLBSSFPeerPubIpAddress OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Public LAN Ip address of this peer entry."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.4.
Name: N/A
Description: alLBSSFPeerMappedPubIpAddress OBJECT-TYPE  SYNTAX IpAddress  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "The NAT'ed Public Ip address of this peer entry."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.5.
Name: alLBSSFPeerActive(5)
Description: alLBSSFPeerActive OBJECT-TYPE  SYNTAX TruthValue  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates if this peer is active or not."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.6.
Name: alLBSSFPeerFaultZone(6)
Description: alLBSSFPeerFaultZone OBJECT-TYPE  SYNTAX Integer32 (0..25)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Indicates which fault zone this peer belongs."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.7.
Name: alLBSSFPeerRole(7)
Description: alLBSSFPeerRole OBJECT-TYPE  SYNTAX DeviceRole  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Role of current peer"
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.8.
Name: alLBSSFPeerDeviceType(8)
Description: alLBSSFPeerDeviceType OBJECT-TYPE  SYNTAX DeviceType  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Device type of this peer."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.9.
Name: alLBSSFPeerLoad(9)
Description: alLBSSFPeerLoad OBJECT-TYPE  SYNTAX Gauge32 (0..100)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Current load of the peer in percentage."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.10.
Name: alLBSSFPeerPriority(10)
Description: alLBSSFPeerPriority OBJECT-TYPE  SYNTAX Integer32 (0..10)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Priority of the peer."
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.11.
Name: N/A
Description: alLBSSFPeerActiveSessions OBJECT-TYPE  SYNTAX Gauge32 (0..100000)  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Number of current active sessions on this peer"
----------------------------------------
OID: 1.3.6.1.4.1.3076.2.1.2.36.2.1.12.
Name: alLBSSFPeerJoinTime(12)
Description: alLBSSFPeerJoinTime OBJECT-TYPE  SYNTAX TimeTicks  MAX-ACCESS read-only  STATUS current  DESCRIPTION  "Time in time-ticks when this peer join the virtual cluster"
----------------------------------------
OID: 1.3.6.1.6.3.10.2.1.1.
Name: snmpEngineID(1)
Description: snmpEngineID OBJECT-TYPE  SYNTAX SnmpEngineID  MAX-ACCESS read-only  STATUS current  DESCRIPTION "An SNMP engine's administratively-unique identifier.  This information SHOULD be stored in non-volatile  storage so that it remains constant across  re-initializations of the SNMP engine."
----------------------------------------
OID: 1.3.6.1.6.3.10.2.1.2.
Name: snmpEngineBoots(2)
Description: snmpEngineBoots OBJECT-TYPE  SYNTAX INTEGER (1..2147483647)  MAX-ACCESS read-only  STATUS current  DESCRIPTION "The number of times that the SNMP engine has  (re-)initialized itself since snmpEngineID  was last configured."
----------------------------------------
OID: 1.3.6.1.6.3.10.2.1.3.
Name: snmpEngineTime(3)
Description: snmpEngineTime OBJECT-TYPE  SYNTAX INTEGER (0..2147483647)  UNITS "seconds"  MAX-ACCESS read-only  STATUS current  DESCRIPTION "The number of seconds since the value of  the snmpEngineBoots object last changed.  When incrementing this object's value would  cause it to exceed its maximum,  snmpEngineBoots is incremented as if a  re-initialization had occurred, and this  object's value consequently reverts to zero."
----------------------------------------
OID: 1.3.6.1.6.3.10.2.1.4.
Name: N/A
Description: snmpEngineMaxMessageSize OBJECT-TYPE  SYNTAX INTEGER (484..2147483647)  MAX-ACCESS read-only  STATUS current  DESCRIPTION "The maximum length in octets of an SNMP message  which this SNMP engine can send or receive and  process, determined as the minimum of the maximum  message size values supported among all of the  transports available to and supported by the engine."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.2.1.2.
Name: snmpTargetAddrTDomain(2)
Description: snmpTargetAddrTDomain OBJECT-TYPE  SYNTAX TDomain  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "This object indicates the transport type of the address  contained in the snmpTargetAddrTAddress object."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.2.1.3.
Name: N/A
Description: snmpTargetAddrTAddress OBJECT-TYPE  SYNTAX TAddress  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "This object contains a transport address. The format of  this address depends on the value of the  snmpTargetAddrTDomain object."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.2.1.4.
Name: snmpTargetAddrTimeout(4)
Description: snmpTargetAddrTimeout OBJECT-TYPE  SYNTAX TimeInterval  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "This object should reflect the expected maximum round  trip time for communicating with the transport address  defined by this row. When a message is sent to this  address, and a response (if one is expected) is not  received within this time period, an implementation  may assume that the response will not be delivered.  Note that the time interval that an application waits  for a response may actually be derived from the value  of this object. The method for deriving the actual time  interval is implementation dependent. One such method  is to derive the expected round trip time based on a  particular retransmission algorithm and on the number  of timeouts which have occurred. The type of message may  also be considered when deriving expected round trip  times for retransmissions. For example, if a message is  being sent with a securityLevel that indicates both  authentication and privacy, the derived value may be  increased to compensate for extra processing time spent  during authentication and encryption processing."  DEFVAL { 1500 }
----------------------------------------
OID: 1.3.6.1.6.3.12.1.2.1.5.
Name: N/A
Description: snmpTargetAddrRetryCount OBJECT-TYPE  SYNTAX Integer32 (0..255)  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "This object specifies a default number of retries to be  attempted when a response is not received for a generated  message. An application may provide its own retry count,  in which case the value of this object is ignored."  DEFVAL { 3 }
----------------------------------------
OID: 1.3.6.1.6.3.12.1.2.1.6.
Name: snmpTargetAddrTagList(6)
Description: snmpTargetAddrTagList OBJECT-TYPE  SYNTAX SnmpTagList  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "This object contains a list of tag values which are  used to select target addresses for a particular  operation."  DEFVAL { "" }
----------------------------------------
OID: 1.3.6.1.6.3.12.1.2.1.7.
Name: snmpTargetAddrParams(7)
Description: snmpTargetAddrParams OBJECT-TYPE  SYNTAX SnmpAdminString (SIZE(1..32))  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The value of this object identifies an entry in the  snmpTargetParamsTable. The identified entry  contains SNMP parameters to be used when generating  messages to be sent to this transport address."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.2.1.8.
Name: N/A
Description: snmpTargetAddrStorageType OBJECT-TYPE  SYNTAX StorageType  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not  allow write-access to any columnar objects in the row."  DEFVAL { nonVolatile }
----------------------------------------
OID: 1.3.6.1.6.3.12.1.2.1.9.
Name: N/A
Description: snmpTargetAddrRowStatus OBJECT-TYPE  SYNTAX RowStatus  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The status of this conceptual row.  To create a row in this table, a manager must  set this object to either createAndGo(4) or  createAndWait(5).  Until instances of all corresponding columns are  appropriately configured, the value of the  corresponding instance of the snmpTargetAddrRowStatus  column is 'notReady'.  In particular, a newly created row cannot be made  active until the corresponding instances of  snmpTargetAddrTDomain, snmpTargetAddrTAddress, and  snmpTargetAddrParams have all been set.  The following objects may not be modified while the  value of this object is active(1):  - snmpTargetAddrTDomain  - snmpTargetAddrTAddress  An attempt to set these objects while the value of  snmpTargetAddrRowStatus is active(1) will result in  an inconsistentValue error."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.3.1.2.
Name: N/A
Description: snmpTargetParamsMPModel OBJECT-TYPE  SYNTAX SnmpMessageProcessingModel  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The Message Processing Model to be used when generating  SNMP messages using this entry."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.3.1.3.
Name: N/A
Description: snmpTargetParamsSecurityModel OBJECT-TYPE  SYNTAX SnmpSecurityModel (1..2147483647)  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The Security Model to be used when generating SNMP  messages using this entry. An implementation may  choose to return an inconsistentValue error if an  attempt is made to set this variable to a value  for a security model which the implementation does  not support."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.3.1.4.
Name: N/A
Description: snmpTargetParamsSecurityName OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The securityName which identifies the Principal on  whose behalf SNMP messages will be generated using  this entry."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.3.1.5.
Name: N/A
Description: snmpTargetParamsSecurityLevel OBJECT-TYPE  SYNTAX SnmpSecurityLevel  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The Level of Security to be used when generating  SNMP messages using this entry."
----------------------------------------
OID: 1.3.6.1.6.3.12.1.3.1.6.
Name: N/A
Description: snmpTargetParamsStorageType OBJECT-TYPE  SYNTAX StorageType  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not  allow write-access to any columnar objects in the row."  DEFVAL { nonVolatile }
----------------------------------------
OID: 1.3.6.1.6.3.12.1.3.1.7.
Name: N/A
Description: snmpTargetParamsRowStatus OBJECT-TYPE  SYNTAX RowStatus  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The status of this conceptual row.  To create a row in this table, a manager must  set this object to either createAndGo(4) or  createAndWait(5).  Until instances of all corresponding columns are  appropriately configured, the value of the  corresponding instance of the snmpTargetParamsRowStatus  column is 'notReady'.  In particular, a newly created row cannot be made  active until the corresponding  snmpTargetParamsMPModel,  snmpTargetParamsSecurityModel,  snmpTargetParamsSecurityName,  and snmpTargetParamsSecurityLevel have all been set.  The following objects may not be modified while the  value of this object is active(1):  - snmpTargetParamsMPModel  - snmpTargetParamsSecurityModel  - snmpTargetParamsSecurityName  - snmpTargetParamsSecurityLevel  An attempt to set these objects while the value of  snmpTargetParamsRowStatus is active(1) will result in  an inconsistentValue error."
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.3.
Name: usmUserSecurityName(3)
Description: usmUserSecurityName OBJECT-TYPE  SYNTAX SnmpAdminString  MAX-ACCESS read-only  STATUS current  DESCRIPTION "A human readable string representing the user in  Security Model independent format.  The default transformation of the User-based Security  Model dependent security ID to the securityName and  vice versa is the identity function so that the  securityName is the same as the userName."
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.4.
Name: usmUserCloneFrom(4)
Description: usmUserCloneFrom OBJECT-TYPE  SYNTAX RowPointer  MAX-ACCESS read-create  STATUS current  DESCRIPTION "A pointer to another conceptual row in this  usmUserTable. The user in this other conceptual  row is called the clone-from user.  When a new user is created (i.e., a new conceptual  row is instantiated in this table), the privacy and  authentication parameters of the new user must be  cloned from its clone-from user. These parameters are:  - authentication protocol (usmUserAuthProtocol)  - privacy protocol (usmUserPrivProtocol)  They will be copied regardless of what the current  value is.  Cloning also causes the initial values of the secret  authentication key (authKey) and the secret encryption  key (privKey) of the new user to be set to the same  values as the corresponding secrets of the clone-from  user to allow the KeyChange process to occur as  required during user creation.  The first time an instance of this object is set by  a management operation (either at or after its  instantiation), the cloning process is invoked.  Subsequent writes are successful but invoke no  action to be taken by the receiver.  The cloning process fails with an 'inconsistentName'  error if the conceptual row representing the  clone-from user does not exist or is not in an active  state when the cloning process is invoked.  When this object is read, the ZeroDotZero OID  is returned."
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.5.
Name: usmUserAuthProtocol(5)
Description: usmUserAuthProtocol OBJECT-TYPE  SYNTAX AutonomousType  MAX-ACCESS read-create  STATUS current  DESCRIPTION "An indication of whether messages sent on behalf of  this user to/from the SNMP engine identified by  usmUserEngineID, can be authenticated, and if so,  the type of authentication protocol which is used.  An instance of this object is created concurrently  with the creation of any other object instance for  the same user (i.e., as part of the processing of  the set operation which creates the first object  instance in the same conceptual row).  If an initial set operation (i.e. at row creation time)  tries to set a value for an unknown or unsupported  protocol, then a 'wrongValue' error must be returned.  The value will be overwritten/set when a set operation  is performed on the corresponding instance of  usmUserCloneFrom.  Once instantiated, the value of such an instance of  this object can only be changed via a set operation to  the value of the usmNoAuthProtocol.  If a set operation tries to change the value of an  existing instance of this object to any value other  than usmNoAuthProtocol, then an 'inconsistentValue'  error must be returned.  If a set operation tries to set the value to the  usmNoAuthProtocol while the usmUserPrivProtocol value  in the same row is not equal to usmNoPrivProtocol,  then an 'inconsistentValue' error must be returned.  That means that an SNMP command generator application  must first ensure that the usmUserPrivProtocol is set  to the usmNoPrivProtocol value before it can set  the usmUserAuthProtocol value to usmNoAuthProtocol."  DEFVAL { usmNoAuthProtocol }
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.6.
Name: usmUserAuthKeyChange(6)
Description: usmUserAuthKeyChange OBJECT-TYPE  SYNTAX KeyChange -- typically (SIZE (0 | 32)) for HMACMD5  -- typically (SIZE (0 | 40)) for HMACSHA  MAX-ACCESS read-create  STATUS current  DESCRIPTION "An object, which when modified, causes the secret  authentication key used for messages sent on behalf  of this user to/from the SNMP engine identified by  usmUserEngineID, to be modified via a one-way  function.  The associated protocol is the usmUserAuthProtocol.  The associated secret key is the user's secret  authentication key (authKey). The associated hash  algorithm is the algorithm used by the user's  usmUserAuthProtocol.  When creating a new user, it is an 'inconsistentName'  error for a set operation to refer to this object  unless it is previously or concurrently initialized  through a set operation on the corresponding instance  of usmUserCloneFrom.  When the value of the corresponding usmUserAuthProtocol  is usmNoAuthProtocol, then a set is successful, but  effectively is a no-op.  When this object is read, the zero-length (empty)  string is returned.  The recommended way to do a key change is as follows:  1) GET(usmUserSpinLock.0) and save in sValue.  2) generate the keyChange value based on the old  (existing) secret key and the new secret key,  let us call this kcValue.  If you do the key change on behalf of another user:  3) SET(usmUserSpinLock.0=sValue,  usmUserAuthKeyChange=kcValue  usmUserPublic=randomValue)  If you do the key change for yourself:  4) SET(usmUserSpinLock.0=sValue,  usmUserOwnAuthKeyChange=kcValue  usmUserPublic=randomValue)  If you get a response with error-status of noError,  then the SET succeeded and the new key is active.  If you do not get a response, then you can issue a  GET(usmUserPublic) and check if the value is equal  to the randomValue you did send in the SET. If so, then  the key change succeeded and the new key is active  (probably the response got lost). If not, then the SET  request probably never reached the target and so you  can start over with the procedure above."  DEFVAL { ''H } -- the empty string
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.7.
Name: N/A
Description: usmUserOwnAuthKeyChange OBJECT-TYPE  SYNTAX KeyChange -- typically (SIZE (0 | 32)) for HMACMD5  -- typically (SIZE (0 | 40)) for HMACSHA  MAX-ACCESS read-create  STATUS current  DESCRIPTION "Behaves exactly as usmUserAuthKeyChange, with one  notable difference: in order for the set operation  to succeed, the usmUserName of the operation  requester must match the usmUserName that  indexes the row which is targeted by this  operation.  In addition, the USM security model must be  used for this operation.  The idea here is that access to this column can be  public, since it will only allow a user to change  his own secret authentication key (authKey).  Note that this can only be done once the row is active.  When a set is received and the usmUserName of the  requester is not the same as the umsUserName that  indexes the row which is targeted by this operation,  then a 'noAccess' error must be returned.  When a set is received and the security model in use  is not USM, then a 'noAccess' error must be returned."  DEFVAL { ''H } -- the empty string
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.8.
Name: usmUserPrivProtocol(8)
Description: usmUserPrivProtocol OBJECT-TYPE  SYNTAX AutonomousType  MAX-ACCESS read-create  STATUS current  DESCRIPTION "An indication of whether messages sent on behalf of  this user to/from the SNMP engine identified by  usmUserEngineID, can be protected from disclosure,  and if so, the type of privacy protocol which is used.  An instance of this object is created concurrently  with the creation of any other object instance for  the same user (i.e., as part of the processing of  the set operation which creates the first object  instance in the same conceptual row).  If an initial set operation (i.e. at row creation time)  tries to set a value for an unknown or unsupported  protocol, then a 'wrongValue' error must be returned.  The value will be overwritten/set when a set operation  is performed on the corresponding instance of  usmUserCloneFrom.  Once instantiated, the value of such an instance of  this object can only be changed via a set operation to  the value of the usmNoPrivProtocol.  If a set operation tries to change the value of an  existing instance of this object to any value other  than usmNoPrivProtocol, then an 'inconsistentValue'  error must be returned.  Note that if any privacy protocol is used, then you  must also use an authentication protocol. In other  words, if usmUserPrivProtocol is set to anything else  than usmNoPrivProtocol, then the corresponding instance  of usmUserAuthProtocol cannot have a value of  usmNoAuthProtocol. If it does, then an  'inconsistentValue' error must be returned."  DEFVAL { usmNoPrivProtocol }
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.9.
Name: usmUserPrivKeyChange(9)
Description: usmUserPrivKeyChange OBJECT-TYPE  SYNTAX KeyChange -- typically (SIZE (0 | 32)) for DES  MAX-ACCESS read-create  STATUS current  DESCRIPTION "An object, which when modified, causes the secret  encryption key used for messages sent on behalf  of this user to/from the SNMP engine identified by  usmUserEngineID, to be modified via a one-way  function.  The associated protocol is the usmUserPrivProtocol.  The associated secret key is the user's secret  privacy key (privKey). The associated hash  algorithm is the algorithm used by the user's  usmUserAuthProtocol.  When creating a new user, it is an 'inconsistentName'  error for a set operation to refer to this object  unless it is previously or concurrently initialized  through a set operation on the corresponding instance  of usmUserCloneFrom.  When the value of the corresponding usmUserPrivProtocol  is usmNoPrivProtocol, then a set is successful, but  effectively is a no-op.  When this object is read, the zero-length (empty)  string is returned.  See the description clause of usmUserAuthKeyChange for  a recommended procedure to do a key change."  DEFVAL { ''H } -- the empty string
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.10.
Name: N/A
Description: usmUserOwnPrivKeyChange OBJECT-TYPE  SYNTAX KeyChange -- typically (SIZE (0 | 32)) for DES  MAX-ACCESS read-create  STATUS current  DESCRIPTION "Behaves exactly as usmUserPrivKeyChange, with one  notable difference: in order for the Set operation  to succeed, the usmUserName of the operation  requester must match the usmUserName that indexes  the row which is targeted by this operation.  In addition, the USM security model must be  used for this operation.  The idea here is that access to this column can be  public, since it will only allow a user to change  his own secret privacy key (privKey).  Note that this can only be done once the row is active.  When a set is received and the usmUserName of the  requester is not the same as the umsUserName that  indexes the row which is targeted by this operation,  then a 'noAccess' error must be returned.  When a set is received and the security model in use  is not USM, then a 'noAccess' error must be returned."  DEFVAL { ''H } -- the empty string
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.11.
Name: usmUserPublic(11)
Description: usmUserPublic OBJECT-TYPE  SYNTAX OCTET STRING (SIZE(0..32))  MAX-ACCESS read-create  STATUS current  DESCRIPTION "A publicly-readable value which can be written as part  of the procedure for changing a user's secret  authentication and/or privacy key, and later read to  determine whether the change of the secret was  effected."  DEFVAL { ''H } -- the empty string
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.12.
Name: usmUserStorageType(12)
Description: usmUserStorageType OBJECT-TYPE  SYNTAX StorageType  MAX-ACCESS read-create  STATUS current  DESCRIPTION "The storage type for this conceptual row.  Conceptual rows having the value 'permanent' must  allow write-access at a minimum to:  - usmUserAuthKeyChange, usmUserOwnAuthKeyChange  and usmUserPublic for a user who employs  authentication, and  - usmUserPrivKeyChange, usmUserOwnPrivKeyChange  and usmUserPublic for a user who employs  privacy.  Note that any user who employs authentication or  privacy must allow its secret(s) to be updated and  thus cannot be 'readOnly'.  If an initial set operation tries to set the value to  'readOnly' for a user who employs authentication or  privacy, then an 'inconsistentValue' error must be  returned. Note that if the value has been previously  set (implicit or explicit) to any value, then the rules  as defined in the StorageType Textual Convention apply.  It is an implementation issue to decide if a SET for  a readOnly or permanent row is accepted at all. In some  contexts this may make sense, in others it may not. If  a SET for a readOnly or permanent row is not accepted  at all, then a 'wrongValue' error must be returned."  DEFVAL { nonVolatile }
----------------------------------------
OID: 1.3.6.1.6.3.15.1.2.2.1.13.
Name: usmUserStatus(13)
Description: usmUserStatus OBJECT-TYPE  SYNTAX RowStatus  MAX-ACCESS read-create  STATUS current  DESCRIPTION "The status of this conceptual row.  Until instances of all corresponding columns are  appropriately configured, the value of the  corresponding instance of the usmUserStatus column  is 'notReady'.  In particular, a newly created row for a user who  employs authentication, cannot be made active until the  corresponding usmUserCloneFrom and usmUserAuthKeyChange  have been set.  Further, a newly created row for a user who also  employs privacy, cannot be made active until the  usmUserPrivKeyChange has been set.  The RowStatus TC [RFC2579] requires that this  DESCRIPTION clause states under which circumstances  other objects in this row can be modified:  The value of this object has no effect on whether  other objects in this conceptual row can be modified,  except for usmUserOwnAuthKeyChange and  usmUserOwnPrivKeyChange. For these 2 objects, the  value of usmUserStatus MUST be active."
----------------------------------------
OID: 1.3.6.1.6.3.16.1.2.1.3.
Name: vacmGroupName(3)
Description: vacmGroupName OBJECT-TYPE  SYNTAX SnmpAdminString (SIZE(1..32))  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The name of the group to which this entry (e.g., the  combination of securityModel and securityName)  belongs.  This groupName is used as index into the  vacmAccessTable to select an access control policy.  However, a value in this table does not imply that an  instance with the value exists in table vacmAccesTable."
----------------------------------------
OID: 1.3.6.1.6.3.16.1.2.1.4.
Name: N/A
Description: vacmSecurityToGroupStorageType OBJECT-TYPE  SYNTAX StorageType  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The storage type for this conceptual row.  Conceptual rows having the value 'permanent' need not  allow write-access to any columnar objects in the row."  DEFVAL {nonVolatile}
----------------------------------------
OID: 1.3.6.1.6.3.16.1.2.1.5.
Name: N/A
Description: vacmSecurityToGroupStatus OBJECT-TYPE  SYNTAX RowStatus  MAX-ACCESS read-create  STATUS current  DESCRIPTION  "The status of this conceptual row.  Until instances of all corresponding columns are  appropriately configured, the value of the  corresponding instance of the vacmSecurityToGroupStatus  column is 'notReady'.  In particular, a newly created row cannot be made  active until a value has been set for vacmGroupName.  The RowStatus TC [RFC2579] requires that this  DESCRIPTION clause states under which circumstances  other objects in this row can be modified:  The value of this object has no effect on whether  other objects in this conceptual row can be modified."
----------------------------------------

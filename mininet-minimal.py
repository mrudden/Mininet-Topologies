# Recreating the mininet minimal topology in Python
# Michael Rudden

from mininet.topo import Topo

class MyMinimal( Topo ):
    "Mininet Minimal Topology"

    def __init__( self ):
        "Recreate Minimal Topology."

        # Initialize topology
        Topo.__init__( self )

        # Add controllers
        controller1 = self.addController( 'c1' )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        switch1 = self.addSwitch( 's1' )

        # Add links
        self.addLink( controller1, switch1 )
        self.addLink( host1, switch1 )
        self.addLink( host2, switch1 )


topos = { 'myminimal': ( lambda: MyMinimal() ) }
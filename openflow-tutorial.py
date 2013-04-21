# OpenFlow Tutorial topology
# http://www.openflow.org/wk/index.php/OpenFlow_Tutorial
# Michael Rudden

from mininet.topo import Topo

class OpenFlowTutorial( Topo ):
    "OpenFlow Tutorial Topology"

    def __init__( self ):
        "Creating OpenFlow Tutorial Topology."

        # Initialize topology
        Topo.__init__( self )

        # Add controllers
        controller1 = self.addController( 'c1' )
        controller2 = self.addController( 'c2' )
        controller3 = self.addController( 'c3' )

        # Add hosts and switches
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        webServer = self.addHost( 'h1' )

        # Add links
        self.addLink( switch1, switch2 )
        self.addLink( switch2, switch3 )


topos = { 'oftutorial': ( lambda: OpenFlowTutorial() ) }
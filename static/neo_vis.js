let neoViz;

function draw() {
    var config = {
        containerId: "viz",
        neo4j: {
            serverUrl: "bolt://localhost:7687",
            serverUser: "neo4j",
            serverPassword: "password"
        },
        visConfig: {
            nodes: {
            },
            groups:{
                person: {color:{border:'#5db665', background:'#8DCC93', highlight: {border: "#5db665", background:"#7bc482"}}, shape:"circle", font:{color: "black", size:8, strokeWidth: 0}, size:6},
                movie: {color:{border:'#5d79b6', background:'#8d98cc', highlight: {border: "#5d6cb6", background:"#7b8cc4"}}, shape:"circle", font:{color: "black", size:8, strokeWidth: 0}, size:6},

            }
        },
        labels: {
            Person: {
                label: "name",
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    group: "person"
                    }
                }
            },
            Movie: {
                label: "name",
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    group: "movie"
                    }
                }
            },
        },
        initialCypher: "MATCH (n) RETURN n LIMIT 25"

    };
    neoViz = new NeoVis.default(config);
    neoViz.render();
}
window.onload = draw()
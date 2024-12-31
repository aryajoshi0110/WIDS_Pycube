import vpython as vp
from Cube_Piece import Cube_Piece

class Color_Cube:

    def __init__(self):

        cube_size = vp.vector(1,1,1)

        # # Create the canvas
        bg = vp.canvas(width=1500, height=800, background=vp.color.black)
        all_directions = [
            vp.vector(1,0,0),vp.vector(0,1,0),vp.vector(0,0,1),vp.vector(-1,0,0),vp.vector(0,-1,0),vp.vector(0,0,-1)
        ]
        for vect in all_directions:
            vp.distant_light(direction=vect,color=vp.color.white*0.3)

        Centers , Edges , Vertices = {} , {} , {}

        all_colors = [
            vp.color.red,
            vp.color.orange,
            vp.color.blue,
            vp.color.green,
            vp.color.white,
            vp.color.yellow
        ]
        center_coords = [
            # vp.vector(0, 0, 0),
            vp.vector(0, 1.05, 0),
            vp.vector(0, -1.05, 0),
            vp.vector(1.05, 0, 0),
            vp.vector(-1.05, 0, 0),
            vp.vector(0, 0, 1.05),
            vp.vector(0, 0, -1.05)
        ]
        edge_coords = [
            vp.vector(1.05,1.05,0),
            vp.vector(1.05,-1.05,0),
            vp.vector(-1.05,1.05,0),
            vp.vector(-1.05,-1.05,0),
            vp.vector(1.05,0,1.05),
            vp.vector(1.05,0,-1.05),
            vp.vector(-1.05,0,1.05),
            vp.vector(-1.05,0,-1.05),
            vp.vector(0,1.05,1.05),
            vp.vector(0,1.05,-1.05),
            vp.vector(0,-1.05,1.05),
            vp.vector(0,-1.05,-1.05)
        ]
        vertex_coords = [
            vp.vector(1.05,1.05,1.05),
            vp.vector(1.05,1.05,-1.05),
            vp.vector(1.05,-1.05,1.05),
            vp.vector(1.05,-1.05,-1.05),
            vp.vector(-1.05,1.05,1.05),
            vp.vector(-1.05,1.05,-1.05),
            vp.vector(-1.05,-1.05,1.05),
            vp.vector(-1.05,-1.05,-1.05)
        ]
        def assign_color(all_colors, active_colors):
            return [color if color in active_colors else vp.color.black for color in all_colors]
        
        CenterMost = Cube_Piece(center=vp.vector(0,0,0),size=cube_size,color=[vp.color.black]*6)
        
        center_map = {
            0: ('Up', [vp.color.white]),
            1: ('Down', [vp.color.yellow]),
            2: ('Front Right', [vp.color.blue]),
            3: ('Back Left', [vp.color.green]),
            4: ('Front Left', [vp.color.red]),
            5: ('Back Right', [vp.color.orange]),
        }

        for i, coord in enumerate(center_coords):
            name, active_colors = center_map[i]
            c = assign_color(all_colors, active_colors)
            Centers[name] = Cube_Piece(center=coord, size=cube_size, color=c)

        edge_map = {
            0: ('Front Right Up', [vp.color.blue, vp.color.white]),
            1: ('Front Right Down', [vp.color.blue, vp.color.yellow]),
            2: ('Back Left Up', [vp.color.green, vp.color.white]),
            3: ('Back Left Down', [vp.color.green, vp.color.yellow]),
            4: ('Front', [vp.color.red, vp.color.blue]),
            5: ('Right', [vp.color.blue, vp.color.orange]),
            6: ('Left', [vp.color.red, vp.color.green]),
            7: ('Back', [vp.color.green, vp.color.orange]),
            8: ('Front Left Up', [vp.color.red, vp.color.white]),
            9: ('Back Right Up', [vp.color.orange, vp.color.white]),
            10: ('Front Left Down', [vp.color.red, vp.color.yellow]),
            11: ('Back Right Down', [vp.color.orange, vp.color.yellow])
        }
        for i,coord in enumerate(edge_coords):
            name, active_colors = edge_map[i]
            c = assign_color(all_colors, active_colors)
            Edges[name] = Cube_Piece(center=coord,size=cube_size,color=c)

        vertex_map = {
            0: ('Front Up', [vp.color.red, vp.color.blue, vp.color.white]),
            1: ('Right Up', [vp.color.orange, vp.color.blue, vp.color.white]),
            2: ('Front Down', [vp.color.red, vp.color.blue, vp.color.yellow]),
            3: ('Right Down', [vp.color.orange, vp.color.blue, vp.color.yellow]),
            4: ('Left Up', [vp.color.red, vp.color.green, vp.color.white]),
            5: ('Back Up', [vp.color.orange, vp.color.white, vp.color.green]),
            6: ('Left Down', [vp.color.red, vp.color.green, vp.color.yellow]),
            7: ('Back Down', [vp.color.orange, vp.color.green, vp.color.yellow])
        }
        for i,coord in enumerate(vertex_coords):
            name, active_colors = vertex_map[i]
            c = assign_color(all_colors, active_colors)
            Vertices[name] = Cube_Piece(center=coord,size=cube_size,color=c)

        Cube_colors = {
            'Red' : vp.color.red,
            'Orange' : vp.color.orange,
            'Blue' : vp.color.blue,
            'Green' : vp.color.green,
            'White' : vp.color.white,
            'Yellow' : vp.color.yellow
        }
        Cube_Sides = ['Up','Down','Front Right','Front Left','Back Right','Back Left']

        # Adjust the camera to view the cube orthogonally
        bg.camera.pos = vp.vector(4, 4, 4)  # Place the camera along the diagonal
        bg.camera.axis = vp.vector(-4, -4, -4)  # Point the camera toward the origin (center of the cube)
        bg.camera.up = vp.vector(0, 1, 0)  # Keep the "up" direction consistent

        self.Centers = Centers
        self.Edges = Edges
        self.Vertices = Vertices
        self.Colours = Cube_colors
        self.Sides = Cube_Sides
        self.Update_State()

    def Update_State(self):
        Unwrapped = {
                'Up': {
                    'Center': self.Centers['Up'].sides['Up'].color,
                    'Edges': {
                        'Front Right Up': self.Edges['Front Right Up'].sides['Up'].color,
                        'Front Left Up': self.Edges['Front Left Up'].sides['Up'].color,
                        'Back Right Up': self.Edges['Back Right Up'].sides['Up'].color,
                        'Back Left Up': self.Edges['Back Left Up'].sides['Up'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Up'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Up'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Up'].color,
                        'Back Up': self.Vertices['Back Up'].sides['Up'].color
                    }
                },
                'Down': {
                    'Center': self.Centers['Down'].sides['Down'].color,
                    'Edges': {
                        'Front Right Down': self.Edges['Front Right Down'].sides['Down'].color,
                        'Front Left Down': self.Edges['Front Left Down'].sides['Down'].color,
                        'Back Right Down': self.Edges['Back Right Down'].sides['Down'].color,
                        'Back Left Down': self.Edges['Back Left Down'].sides['Down'].color
                    },
                    'Vertices': {
                        'Front Down': self.Vertices['Front Down'].sides['Down'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Down'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Down'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Down'].color
                    }
                },
                'Front Right': {
                    'Center': self.Centers['Front Right'].sides['Right'].color,
                    'Edges': {
                        'Front Right Up': self.Edges['Front Right Up'].sides['Right'].color,
                        'Front Right Down': self.Edges['Front Right Down'].sides['Right'].color,
                        'Front': self.Edges['Front'].sides['Right'].color,
                        'Right': self.Edges['Right'].sides['Right'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Right'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Right'].color,
                        'Front Down': self.Vertices['Front Down'].sides['Right'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Right'].color
                    }
                },
                'Back Left': {
                    'Center': self.Centers['Back Left'].sides['Left'].color,
                    'Edges': {
                        'Back Left Up': self.Edges['Back Left Up'].sides['Left'].color,
                        'Back Left Down': self.Edges['Back Left Down'].sides['Left'].color,
                        'Back': self.Edges['Back'].sides['Left'].color,
                        'Left': self.Edges['Left'].sides['Left'].color
                    },
                    'Vertices': {
                        'Back Up': self.Vertices['Back Up'].sides['Left'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Left'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Left'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Left'].color
                    }
                },
                'Front Left': {
                    'Center': self.Centers['Front Left'].sides['Front'].color,
                    'Edges': {
                        'Front Left Up': self.Edges['Front Left Up'].sides['Front'].color,
                        'Front Left Down': self.Edges['Front Left Down'].sides['Front'].color,
                        'Front': self.Edges['Front'].sides['Front'].color,
                        'Left': self.Edges['Left'].sides['Front'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Front'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Front'].color,
                        'Front Down': self.Vertices['Front Down'].sides['Front'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Front'].color
                    }
                },
                'Back Right': {
                    'Center': self.Centers['Back Right'].sides['Back'].color,
                    'Edges': {
                        'Back Right Up': self.Edges['Back Right Up'].sides['Back'].color,
                        'Back Right Down': self.Edges['Back Right Down'].sides['Back'].color,
                        'Back': self.Edges['Back'].sides['Back'].color,
                        'Right': self.Edges['Right'].sides['Back'].color
                    },
                    'Vertices': {
                        'Back Up': self.Vertices['Back Up'].sides['Back'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Back'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Back'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Back'].color
                    }
                }
            }   
        self.State = Unwrapped


class Mirror_Cube:

    def __init__(self):

        cube_size = vp.vector(1,1,1)

        # # Create the canvas
        bg = vp.canvas(width=1500, height=800, background=vp.color.black)
        all_directions = [
            vp.vector(1,0,0),vp.vector(0,1,0),vp.vector(-1,0,0),vp.vector(0,-1,0),vp.vector(0,0,-1)
        ]
        for vect in all_directions:
            vp.distant_light(direction=vect,color=vp.color.white*0.75)
        vp.distant_light(direction=vp.vector(0,0,1),color=vp.color.white*0.5)

        Centers , Edges , Vertices = {} , {} , {}
        center_coord_size = [
            # vp.vector(0, 0, 0),
            [vp.vector(0, 0.8, 0),vp.vector(1,0.4,1)],
            [vp.vector(0, -1.3, 0),vp.vector(1,1.4,1)],
            [vp.vector(1.1, 0, 0),vp.vector(1,1,1)],
            [vp.vector(-1, 0, 0),vp.vector(0.8,1,1)],
            [vp.vector(0, 0, 1.2),vp.vector(1,1,1.2)],
            [vp.vector(0, 0, -0.9),vp.vector(1,1,0.6)]
        ]
        edge_coord_size = [
            [vp.vector(1.1,0.8,0),vp.vector(1,0.4,1)],
            [vp.vector(1.1,-1.3,0),vp.vector(1,1.4,1)],
            [vp.vector(-1,0.8,0),vp.vector(0.8,0.4,1)],
            [vp.vector(-1,-1.3,0),vp.vector(0.8,1.4,1)],
            [vp.vector(1.1,0,1.2),vp.vector(1,1,1.2)],
            [vp.vector(1.1,0,-0.9),vp.vector(1,1,0.6)],
            [vp.vector(-1,0,1.2),vp.vector(0.8,1,1.2)],
            [vp.vector(-1,0,-0.9),vp.vector(0.8,1,0.6)],
            [vp.vector(0,0.8,1.2),vp.vector(1,0.4,1.2)],
            [vp.vector(0,0.8,-0.9),vp.vector(1,0.4,0.6)],
            [vp.vector(0,-1.3,1.2),vp.vector(1,1.4,1.2)],
            [vp.vector(0,-1.3,-0.9),vp.vector(1,1.4,0.6)]
        ]
        vertex_coord_size = [
            [vp.vector(1.1,0.8,1.2),vp.vector(1,0.4,1.2)],
            [vp.vector(1.1,0.8,-0.9),vp.vector(1,0.4,0.6)],
            [vp.vector(1.1,-1.3,1.2),vp.vector(1,1.4,1.2)],
            [vp.vector(1.1,-1.3,-0.9),vp.vector(1,1.4,0.6)],
            [vp.vector(-1,0.8,1.2),vp.vector(0.8,0.4,1.2)],
            [vp.vector(-1,0.8,-0.9),vp.vector(0.8,0.4,0.6)],
            [vp.vector(-1,-1.3,1.2),vp.vector(0.8,1.4,1.2)],
            [vp.vector(-1,-1.3,-0.9),vp.vector(0.8,1.4,0.6)]
        ]
        i = 0
        CenterMost = Cube_Piece(center=vp.vector(0,0,0),size=cube_size,color=[vp.color.black]*6)
        def assign_color(all_colors, active_colors):
            return [color if color in active_colors else vp.color.black for color in all_colors]
        blk = vp.vector(0,0,0)
        silver = vp.vector(0.5,0.5,0.5)
        s1 , s2 , s3 , s4 , s5 , s6 = vp.vector(0.51,0.5,0.5),vp.vector(0.49,0.5,0.5),vp.vector(0.5,0.51,0.5),vp.vector(0.5,0.49,0.5),vp.vector(0.5,0.5,0.51),vp.vector(0.5,0.5,0.49)
        #vp.color.white,vp.color.yellow,vp.color.blue,vp.color.green,vp.color.red,vp.color.orange
        all_colors = [s5,s6,s3,s4,s1,s2]
        center_map = {
            0: ('Up', [s1]),
            1: ('Down', [s2]),
            2: ('Front Right', [s3]),
            3: ('Back Left', [s4]),
            4: ('Front Left', [s5]),
            5: ('Back Right', [s6]),
        }
        for i, coord_size in enumerate(center_coord_size):
            name, active_colors = center_map[i]
            c = assign_color(all_colors, active_colors)
            Centers[name] = Cube_Piece(center=coord_size[0],size=coord_size[1],color=c)

        edge_map = {
            0: ('Front Right Up', [s3, s1]),
            1: ('Front Right Down', [s3, s2]),
            2: ('Back Left Up', [s4, s1]),
            3: ('Back Left Down', [s4, s2]),
            4: ('Front', [s5, s3]),
            5: ('Right', [s3, s6]),
            6: ('Left', [s5, s4]),
            7: ('Back', [s4, s6]),
            8: ('Front Left Up', [s5, s1]),
            9: ('Back Right Up', [s6, s1]),
            10: ('Front Left Down', [s5, s2]),
            11: ('Back Right Down', [s6, s2])
        }

        for i, coord_size in enumerate(edge_coord_size):
            name, active_colors = edge_map[i]
            c = assign_color(all_colors, active_colors)
            Edges[name] = Cube_Piece(center=coord_size[0],size=coord_size[1],color=c)

        vertex_map = {
            0: ('Front Up', [s5, s3, s1]),
            1: ('Right Up', [s6, s3, s1]),
            2: ('Front Down', [s5, s3, s2]),
            3: ('Right Down', [s6, s3, s2]),
            4: ('Left Up', [s5, s4, s1]),
            5: ('Back Up', [s6, s1, s4]),
            6: ('Left Down', [s5, s4, s2]),
            7: ('Back Down', [s6, s4, s2])
        }

        for i, coord_size in enumerate(vertex_coord_size):
            name, active_colors = vertex_map[i]
            c = assign_color(all_colors, active_colors)
            Vertices[name] = Cube_Piece(center=coord_size[0],size=coord_size[1],color=c)
            
        # Adjust the camera to view the cube orthogonally
        bg.camera.pos = vp.vector(4.5, 3.5, 4.5)  # Place the camera along the diagonal
        bg.camera.axis = vp.vector(-4, -4, -4)  # Point the camera toward the origin (center of the cube)
        bg.camera.up = vp.vector(0, 1, 0)  # Keep the "up" direction consistent

        Cube_colors = {
            'Red' : s5,
            'Orange' : s6,
            'Blue' : s3,
            'Green' : s4,
            'White' : s1,
            'Yellow' : s2
            }
        Cube_Sides = ['Up','Down','Front Right','Front Left','Back Right','Back Left']

        self.Centers = Centers
        self.Edges = Edges
        self.Vertices = Vertices
        self.Colours = Cube_colors
        self.Sides = Cube_Sides
        self.Update_State()

    def Update_State(self):
        Unwrapped = {
                'Up': {
                    'Center': self.Centers['Up'].sides['Up'].color,
                    'Edges': {
                        'Front Right Up': self.Edges['Front Right Up'].sides['Up'].color,
                        'Front Left Up': self.Edges['Front Left Up'].sides['Up'].color,
                        'Back Right Up': self.Edges['Back Right Up'].sides['Up'].color,
                        'Back Left Up': self.Edges['Back Left Up'].sides['Up'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Up'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Up'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Up'].color,
                        'Back Up': self.Vertices['Back Up'].sides['Up'].color
                    }
                },
                'Down': {
                    'Center': self.Centers['Down'].sides['Down'].color,
                    'Edges': {
                        'Front Right Down': self.Edges['Front Right Down'].sides['Down'].color,
                        'Front Left Down': self.Edges['Front Left Down'].sides['Down'].color,
                        'Back Right Down': self.Edges['Back Right Down'].sides['Down'].color,
                        'Back Left Down': self.Edges['Back Left Down'].sides['Down'].color
                    },
                    'Vertices': {
                        'Front Down': self.Vertices['Front Down'].sides['Down'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Down'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Down'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Down'].color
                    }
                },
                'Front Right': {
                    'Center': self.Centers['Front Right'].sides['Right'].color,
                    'Edges': {
                        'Front Right Up': self.Edges['Front Right Up'].sides['Right'].color,
                        'Front Right Down': self.Edges['Front Right Down'].sides['Right'].color,
                        'Front': self.Edges['Front'].sides['Right'].color,
                        'Right': self.Edges['Right'].sides['Right'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Right'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Right'].color,
                        'Front Down': self.Vertices['Front Down'].sides['Right'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Right'].color
                    }
                },
                'Back Left': {
                    'Center': self.Centers['Back Left'].sides['Left'].color,
                    'Edges': {
                        'Back Left Up': self.Edges['Back Left Up'].sides['Left'].color,
                        'Back Left Down': self.Edges['Back Left Down'].sides['Left'].color,
                        'Back': self.Edges['Back'].sides['Left'].color,
                        'Left': self.Edges['Left'].sides['Left'].color
                    },
                    'Vertices': {
                        'Back Up': self.Vertices['Back Up'].sides['Left'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Left'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Left'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Left'].color
                    }
                },
                'Front Left': {
                    'Center': self.Centers['Front Left'].sides['Front'].color,
                    'Edges': {
                        'Front Left Up': self.Edges['Front Left Up'].sides['Front'].color,
                        'Front Left Down': self.Edges['Front Left Down'].sides['Front'].color,
                        'Front': self.Edges['Front'].sides['Front'].color,
                        'Left': self.Edges['Left'].sides['Front'].color
                    },
                    'Vertices': {
                        'Front Up': self.Vertices['Front Up'].sides['Front'].color,
                        'Left Up': self.Vertices['Left Up'].sides['Front'].color,
                        'Front Down': self.Vertices['Front Down'].sides['Front'].color,
                        'Left Down': self.Vertices['Left Down'].sides['Front'].color
                    }
                },
                'Back Right': {
                    'Center': self.Centers['Back Right'].sides['Back'].color,
                    'Edges': {
                        'Back Right Up': self.Edges['Back Right Up'].sides['Back'].color,
                        'Back Right Down': self.Edges['Back Right Down'].sides['Back'].color,
                        'Back': self.Edges['Back'].sides['Back'].color,
                        'Right': self.Edges['Right'].sides['Back'].color
                    },
                    'Vertices': {
                        'Back Up': self.Vertices['Back Up'].sides['Back'].color,
                        'Right Up': self.Vertices['Right Up'].sides['Back'].color,
                        'Back Down': self.Vertices['Back Down'].sides['Back'].color,
                        'Right Down': self.Vertices['Right Down'].sides['Back'].color
                    }
                }
            }   
        self.State = Unwrapped


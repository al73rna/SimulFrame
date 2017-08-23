import pyglet

window = pyglet.window.Window()


## Black : 0
## White : 1
## Green : 2
## Blue  : 3
## Red   : 4

color_green = ('c3B', (0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0))
color_blue  = ('c3B', (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255))
color_red   = ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0))

def print_array(input_array, pixel_size):
	for i in range(len(input_array)):
		for j in range(len(input_array[i])):
			if input_array[i][j] == 1:
				pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (pixel_size*j,pixel_size*i,
																	 pixel_size*j,pixel_size*(i+1), 
																	 pixel_size*(j+1),pixel_size*(i+1), 
																	 pixel_size*(j+1),pixel_size*i)))
			elif input_array[i][j] == 2:
				pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (pixel_size*j,pixel_size*i,
																	 pixel_size*j,pixel_size*(i+1), 
																	 pixel_size*(j+1),pixel_size*(i+1), 
																	 pixel_size*(j+1),pixel_size*i)), color_green)
			elif input_array[i][j] == 3:
				pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (pixel_size*j,pixel_size*i,
																	 pixel_size*j,pixel_size*(i+1), 
																	 pixel_size*(j+1),pixel_size*(i+1), 
																	 pixel_size*(j+1),pixel_size*i)), color_blue)
			elif input_array[i][j] == 4:
				pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (pixel_size*j,pixel_size*i,
																	 pixel_size*j,pixel_size*(i+1), 
																	 pixel_size*(j+1),pixel_size*(i+1), 
																	 pixel_size*(j+1),pixel_size*i)), color_red)

my_array = [[0,1,0,1,0,1,0,1,0,1],
			[1,0,4,0,3,0,2,2,1,0],
			[0,1,0,1,3,1,0,1,0,1],
			[1,0,1,3,1,0,1,0,1,0],
			[1,1,1,1,4,1,1,1,1,1],
			[1,0,1,0,2,0,3,0,1,0],
			[0,1,0,1,0,1,0,1,0,1],
			[1,0,1,0,1,0,1,0,1,0],
			[0,1,4,4,0,1,2,2,0,1],
			[1,0,1,0,1,0,1,2,1,0]]


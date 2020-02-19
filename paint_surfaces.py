# Paint Surfaces
# Created by Acaran (2020)
# acaran101.wordpress.com

displayName = "Paint Surfaces"

inputs = (
	("Replaces any block exposed to air with a selected block.","label"),
	("Paint With", "blocktype"),
	("Paint On (Replace)", "blocktype"),
	("Replace any Block", False),
	("Don't Place Data (faster)", True)
)

def perform(level, box, options):
	block = options["Paint With"].ID
	data = options["Paint With"].blockData
	replace = options["Paint On (Replace)"].ID
	replaceData = options["Paint On (Replace)"].blockData
	anyBlock = options["Replace any Block"]
	dontData = options["Don't Place Data (faster)"]

	# Python effiency optimizations (try running this function on 10 000 000 blocks...)
	bAt = level.blockAt
	sbAt = level.setBlockAt
	sbdAt = level.setBlockDataAt

	if dontData == True:
		if (anyBlock == True):
			for x in xrange(box.minx, box.maxx):
				for y in xrange(box.miny, box.maxy):
					for z in xrange(box.minz, box.maxz):
						if bAt(x, y, z) != 0:
							if bAt(x+1, y, z) == 0 or bAt(x-1, y, z) == 0 or bAt(x, y+1, z) == 0 or bAt(x, y-1, z) == 0 or bAt(x, y, z+1) == 0 or bAt(x, y, z-1) == 0:
								sbAt(x, y, z, block)
		else:
			for x in xrange(box.minx, box.maxx):
				for y in xrange(box.miny, box.maxy):
					for z in xrange(box.minz, box.maxz):
						if bAt(x, y, z) == replace:
							if bAt(x+1, y, z) == 0 or bAt(x-1, y, z) == 0 or bAt(x, y+1, z) == 0 or bAt(x, y-1, z) == 0 or bAt(x, y, z+1) == 0 or bAt(x, y, z-1) == 0:
								sbAt(x, y, z, block)
	else:
		if (anyBlock == True):
			for x in xrange(box.minx, box.maxx):
				for y in xrange(box.miny, box.maxy):
					for z in xrange(box.minz, box.maxz):
						if bAt(x, y, z) != 0:
							if bAt(x+1, y, z) == 0 or bAt(x-1, y, z) == 0 or bAt(x, y+1, z) == 0 or bAt(x, y-1, z) == 0 or bAt(x, y, z+1) == 0 or bAt(x, y, z-1) == 0:
								sbAt(x, y, z, block)
								sbdAt(x, y, z, data)

		else:
			for x in xrange(box.minx, box.maxx):
				for y in xrange(box.miny, box.maxy):
					for z in xrange(box.minz, box.maxz):
						if bAt(x, y, z) == replace:
							if bAt(x+1, y, z) == 0 or bAt(x-1, y, z) == 0 or bAt(x, y+1, z) == 0 or bAt(x, y-1, z) == 0 or bAt(x, y, z+1) == 0 or bAt(x, y, z-1) == 0:
								sbAt(x, y, z, block)
								sbdAt(x, y, z, data)
	
	level.markDirtyBox(box)

from typing import List, Any, Optional
import math
import copy
from typing import Any, List
import unittest
from dataclasses import dataclass

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
	def centervalue(l):
		l = [str(item) for item in l]
		largest = max(l, key=len)
		return len(largest)+2
		
	finalstring =""
	if centered == True:
		columns = len(rows[0])
		dictionaryoflists = []
		for x in range(columns):
			sublist = []
			if labels is not None:
				sublist.append(labels[x])
			sublist += [item[x] for item in rows]
			dictionaryoflists.append(sublist)



		centervalues = []
		for z in dictionaryoflists:
			centervalues.append(centervalue(z))


		##TOPBORDER
		hidashes = "┌"
		for x in range(columns):
			if x == 0:
				hidashes+= "─".center(centervalues[x], "─")
			else:
				hidashes+= "┬"+"─".center(centervalues[x], "─")
		hidashes+="┐"
		finalstring+=hidashes
		if labels is not None:
		##LABELS
			labell = "│"
			for x in range(columns):
				if x == 0:
					labell+= str(labels[x]).center(centervalues[x])
				else:
					labell+="│" + str(labels[x]).center(centervalues[x])
			labell+="│"
			finalstring+="\n"+labell
			##sepborder
			sepborder = "├"
			for x in range(columns):
				if x == 0:
					sepborder+= "─".center(centervalues[x], "─")
				else:
					sepborder+= "┼"+"─".center(centervalues[x], "─")
					
			sepborder+="┤"
			finalstring+="\n"+sepborder

		##printrows
		for z in rows:
			rowstring = "│"
			for x in range(columns):
				if x == 0:
					rowstring+= str(z[x]).center(centervalues[x])
				else:
					rowstring+="│" + str(z[x]).center(centervalues[x])
			rowstring+="│"
			finalstring+="\n"+rowstring

		##LOWBORDER
		lowdashes = "└"
		for x in range(columns):
			if x == 0:
				lowdashes+= "─".center(centervalues[x], "─")
			else:
				lowdashes+= "┴"+"─".center(centervalues[x], "─")
				
		lowdashes+="┘"

		finalstring+="\n"+lowdashes
	else:
		columns = len(rows[0])
		dictionaryoflists = []
		for x in range(columns):
			sublist = []
			if labels is not None:
				sublist.append(labels[x])
			sublist += [item[x] for item in rows]
			dictionaryoflists.append(sublist)



		centervalues = []
		for z in dictionaryoflists:
			centervalues.append(centervalue(z))


		##TOPBORDER
		hidashes = "┌"
		for x in range(columns):
			if x == 0:
				hidashes+= "─".ljust(centervalues[x], "─")
			else:
				hidashes+= "┬"+"─".ljust(centervalues[x], "─")
		hidashes+="┐"
		finalstring+=hidashes
		if labels is not None:
		##LABELS
			labell = "│ "
			for x in range(columns):
				if x == 0:
					labell+= str(labels[x]).ljust(centervalues[x]-1)
				else:
					labell+="│ " + str(labels[x]).ljust(centervalues[x]-1)
			labell+="│"
			finalstring+="\n"+labell
			##sepborder
			sepborder = "├"
			for x in range(columns):
				if x == 0:
					sepborder+= "─".ljust(centervalues[x], "─")
				else:
					sepborder+= "┼"+"─".ljust(centervalues[x], "─")
					
			sepborder+="┤"
			finalstring+="\n"+sepborder

		##printrows
		for z in rows:
			rowstring = "│ "
			for x in range(columns):
				if x == 0:
					rowstring+= (str(z[x])).ljust(centervalues[x]-1)
				else:
					rowstring+="│ " + (str(z[x])).ljust(centervalues[x]-1)
			rowstring+="│"
			finalstring+="\n"+rowstring

		##LOWBORDER
		lowdashes = "└"
		for x in range(columns):
			if x == 0:
				lowdashes+= "─".ljust(centervalues[x], "─")
			else:
				lowdashes+= "┴"+"─".ljust(centervalues[x], "─")
				
		lowdashes+="┘"

		finalstring+="\n"+lowdashes
	finalstring+="\n"
	return finalstring


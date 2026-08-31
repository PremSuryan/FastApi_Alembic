# emp table 3 cols id , name , salary 
# returned 3 low sal

# select name , salary from emp order by salary asc  3

"""
select * from emp 
order by salary asc
offset 2
limit 1
"""

# app table 5 cols id, docid , patient id app date status find doc 10 completed in last 30 days 

# data = db.query(Appointment)

"""
select * from Appointment 
where status = 'completed'
and 
Date = currentdate() - 30 
limit 10

"""

# Create a FastAPI endpoint that accepts a document-processing request and returns a job ID instead of waiting 
# for processing to finish.

"""

app = FastAPI()

class File(BaseModel):
	job_id:int
	file_name : str

@app.get("/")
async def file_process(file: File):
	import threading

	data = threading.Thread(target= doc_process,args=File.file_name)
	data.start()
	return {"id":file.job_id}


async def doc_process(file):
      print("file processing")

"""

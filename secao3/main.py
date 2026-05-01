from typing import List, Optional

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models import Curso
 
app = FastAPI()

cursos = {
    1:{
        "titulo": "Programação",
        "aulas":112,
        "horas":50
    }, 
    2:{
        "titulo": "Algoritimos",
        "aulas":10,
        "horas":30
    }
}


@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso_id(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado!'
        )

@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso:Curso):
    next_id:int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso:Curso):
        if curso_id in cursos:
            cursos[curso_id] = curso
            del curso.id
            return curso
        else:
             raise HTTPException(
                  status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe curso com este id {curso_id}"
             )

@app.delete("/cursos/{curso_id}")
async def del_curso(curso_id: int):
    if curso_id in cursos:
          del cursos[curso_id]
          return {"message": f"Curso {curso_id} removido com sucesso"}
    else:
         raise HTTPException(
              status_code=status.HTTP_404_NOT_FOUND, 
              detail=f"Curso não encontrado com o id {curso_id}" 
         )
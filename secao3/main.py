from fastapi import FastAPI

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
    curso = cursos[curso_id]
    curso.update({"id":curso_id})
    return curso
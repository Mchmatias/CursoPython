import json
import os
from typing import Dict, List, Any

DATA_FILE = "alumnos.json"


class StudentManager:
	def __init__(self, path: str = DATA_FILE):
		self.path = path
		self.alumnos: Dict[str, Dict[str, Any]] = {}
		self.load()

	def load(self):
		if not os.path.exists(self.path):
			self.alumnos = {}
			return
		try:
			with open(self.path, "r", encoding="utf-8") as f:
				self.alumnos = json.load(f)
		except Exception:
			print("Advertencia: no se pudo leer el archivo de datos o está corrupto. Se inicializa vacío.")
			self.alumnos = {}

	def save(self):
		try:
			with open(self.path, "w", encoding="utf-8") as f:
				json.dump(self.alumnos, f, ensure_ascii=False, indent=2)
		except Exception as e:
			print(f"Error al guardar los datos: {e}")

	def list_students(self) -> List[Dict[str, Any]]:
		return list(self.alumnos.values())

	def add_student(self, alumno: Dict[str, Any]) -> bool:
		dni = alumno.get("DNI")
		if not dni:
			return False
		if dni in self.alumnos:
			return False
		# initialize fields
		alumno.setdefault("notas", [])
		alumno.setdefault("faltas", 0)
		alumno.setdefault("amonestaciones", 0)
		self.alumnos[dni] = alumno
		self.save()
		return True

	def get_student(self, dni: str) -> Dict[str, Any]:
		return self.alumnos.get(dni)

	def modify_student(self, dni: str, updates: Dict[str, Any]) -> bool:
		if dni not in self.alumnos:
			return False
		self.alumnos[dni].update(updates)
		self.save()
		return True

	def expel_student(self, dni: str) -> bool:
		if dni not in self.alumnos:
			return False
		del self.alumnos[dni]
		self.save()
		return True

	def add_grade(self, dni: str, grade: float) -> bool:
		s = self.get_student(dni)
		if not s:
			return False
		s.setdefault("notas", []).append(grade)
		self.save()
		return True

	def add_absence(self, dni: str, count: int = 1) -> bool:
		s = self.get_student(dni)
		if not s:
			return False
		s["faltas"] = int(s.get("faltas", 0)) + int(count)
		self.save()
		return True

	def add_admonition(self, dni: str, count: int = 1) -> bool:
		s = self.get_student(dni)
		if not s:
			return False
		s["amonestaciones"] = int(s.get("amonestaciones", 0)) + int(count)
		self.save()
		return True


def input_nonempty(prompt: str) -> str:
	while True:
		v = input(prompt).strip()
		if v:
			return v
		print("Entrada vacía. Intente nuevamente.")


def mostrar_alumno(a: Dict[str, Any]):
	print("--- Datos del alumno ---")
	print(f"Nombre: {a.get('Nombre', '')}")
	print(f"Apellido: {a.get('Apellido', '')}")
	print(f"Fecha de nacimiento: {a.get('FechaNacimiento', '')}")
	print(f"DNI: {a.get('DNI', '')}")
	print(f"Tutor: {a.get('Tutor', '')}")
	print(f"Notas: {a.get('notas', [])}")
	print(f"Faltas: {a.get('faltas', 0)}")
	print(f"Amonestaciones: {a.get('amonestaciones', 0)}")
	print("------------------------")


def menu(manager: StudentManager):
	while True:
		print("\nGestor de Alumnos - Menú")
		print("1) Listar todos los alumnos")
		print("2) Mostrar datos de un alumno (por DNI)")
		print("3) Agregar alumno")
		print("4) Modificar datos de alumno")
		print("5) Agregar nota / falta / amonestación")
		print("6) Expulsar alumno")
		print("7) Salir")
		opt = input("Seleccione una opción: ").strip()
		if opt == "1":
			todos = manager.list_students()
			if not todos:
				print("No hay alumnos registrados.")
			for a in todos:
				print(f"{a.get('Apellido','')} {a.get('Nombre','')} - DNI: {a.get('DNI','')}")

		elif opt == "2":
			dni = input_nonempty("DNI: ")
			a = manager.get_student(dni)
			if not a:
				print("Alumno no encontrado.")
			else:
				mostrar_alumno(a)

		elif opt == "3":
			nombre = input_nonempty("Nombre: ")
			apellido = input_nonempty("Apellido: ")
			fn = input_nonempty("Fecha de nacimiento (DD/MM/AAAA): ")
			dni = input_nonempty("DNI: ")
			tutor = input_nonempty("Nombre del tutor: ")
			alumno = {
				"Nombre": nombre,
				"Apellido": apellido,
				"FechaNacimiento": fn,
				"DNI": dni,
				"Tutor": tutor,
				"notas": [],
				"faltas": 0,
				"amonestaciones": 0,
			}
			if manager.add_student(alumno):
				print("Alumno agregado correctamente.")
			else:
				print("No se pudo agregar. DNI ya existente o datos inválidos.")

		elif opt == "4":
			dni = input_nonempty("DNI del alumno a modificar: ")
			a = manager.get_student(dni)
			if not a:
				print("Alumno no encontrado.")
				continue
			print("Dejar vacío para mantener el valor actual.")
			nombre = input("Nombre (actual: {}): ".format(a.get("Nombre", ""))).strip()
			apellido = input("Apellido (actual: {}): ".format(a.get("Apellido", ""))).strip()
			fn = input("Fecha de nacimiento (actual: {}): ".format(a.get("FechaNacimiento", ""))).strip()
			tutor = input("Tutor (actual: {}): ".format(a.get("Tutor", ""))).strip()
			updates = {}
			if nombre:
				updates["Nombre"] = nombre
			if apellido:
				updates["Apellido"] = apellido
			if fn:
				updates["FechaNacimiento"] = fn
			if tutor:
				updates["Tutor"] = tutor
			if updates:
				manager.modify_student(dni, updates)
				print("Datos actualizados.")
			else:
				print("No se realizaron cambios.")

		elif opt == "5":
			dni = input_nonempty("DNI del alumno: ")
			a = manager.get_student(dni)
			if not a:
				print("Alumno no encontrado.")
				continue
			print("a) Agregar nota\nb) Agregar falta\nc) Agregar amonestación")
			sub = input("Seleccione acción: ").strip().lower()
			if sub == "a":
				try:
					grade = float(input_nonempty("Nota (numérica): "))
				except ValueError:
					print("Nota inválida.")
					continue
				manager.add_grade(dni, grade)
				print("Nota agregada.")
			elif sub == "b":
				try:
					c = int(input_nonempty("Cantidad de faltas a agregar (enteros): "))
				except ValueError:
					print("Cantidad inválida.")
					continue
				manager.add_absence(dni, c)
				print("Faltas actualizadas.")
			elif sub == "c":
				try:
					c = int(input_nonempty("Cantidad de amonestaciones a agregar (enteros): "))
				except ValueError:
					print("Cantidad inválida.")
					continue
				manager.add_admonition(dni, c)
				print("Amonestaciones actualizadas.")
			else:
				print("Opción inválida.")

		elif opt == "6":
			dni = input_nonempty("DNI del alumno a expulsar: ")
			confirm = input(f"Confirma expulsar al alumno con DNI {dni}? (s/N): ").strip().lower()
			if confirm == "s":
				if manager.expel_student(dni):
					print("Alumno expulsado (eliminado).")
				else:
					print("Alumno no encontrado.")
			else:
				print("Operación cancelada.")

		elif opt == "7":
			print("Saliendo. Guardando datos...")
			manager.save()
			break
		else:
			print("Opción inválida. Intente de nuevo.")


def main():
	manager = StudentManager()
	menu(manager)


if __name__ == "__main__":
    main()


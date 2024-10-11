from pyscript import Element
import datetime

notizen = []

def render_notizen(filtered_notizen=None):
    container = Element("notizen-container")
    container.clear()
    if filtered_notizen is None:
        filtered_notizen = notizen
    for index, notiz in enumerate(filtered_notizen):
        notiz_element = f"""
        <li class="notiz {'abgeschlossen' if notiz['abgeschlossen'] else ''}">
            <span>{notiz['datum']} - {notiz['beschreibung']}</span>
            <div>
                <button onclick="toggle_abgeschlossen({index})">Toggle Zustand</button>
                <button onclick="loesche_notiz({index})">Löschen</button>
            </div>
        </li>
        """
        container.element.innerHTML += notiz_element
    update_counter()

def update_counter():
    counter = Element("notizen-counter")
    counter.write(f"Anzahl der Notizen: {len(notizen)}")

def add_notiz(event):
    event.preventDefault()
    datum = Element("datum").value
    beschreibung = Element("beschreibung").value
    notizen.append({
        "datum": datum,
        "beschreibung": beschreibung,
        "abgeschlossen": False
    })
    render_notizen()
    close_modal()

def loesche_notiz(index):
    del notizen[index]
    render_notizen()

def toggle_abgeschlossen(index):
    notizen[index]["abgeschlossen"] = not notizen[index]["abgeschlossen"]
    render_notizen()

def open_modal(event):
    modal = Element("notiz-modal")
    modal.element.style.display = "block"

def close_modal(event=None):
    modal = Element("notiz-modal")
    modal.element.style.display = "none"

def filter_notizen():
    filter_value = Element("filter").value
    if filter_value == "completed":
        filtered_notizen = [notiz for notiz in notizen if notiz["abgeschlossen"]]
    elif filter_value == "not_completed":
        filtered_notizen = [notiz for notiz in notizen if not notiz["abgeschlossen"]]
    else:
        filtered_notizen = notizen
    render_notizen(filtered_notizen)

def sort_notizen():
    sort_value = Element("sort").value
    if sort_value == "date":
        sorted_notizen = sorted(notizen, key=lambda x: x["datum"])
    elif sort_value == "description":
        sorted_notizen = sorted(notizen, key=lambda x: x["beschreibung"])
    render_notizen(sorted_notizen)

Element("notiz-form").element.onsubmit = add_notiz
Element("add-notiz-button").element.onclick = open_modal
Element("notiz-modal").element.querySelector(".close-button").onclick = close_modal

render_notizen()
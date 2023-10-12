from __future__ import print_function
from auth import spreadsheet_service
from auth import drive_service

informacion_asistente = {
    "Nombre de la asistente": "Fernanda",
    "¿La asistente mencionó el precio de los departamentos?": "Sí",
    "Detalles específicos sobre el precio de los departamentos proporcionados por la asistente": "El costo de los departamentos es de 3.1 millones de pesos.",
    "¿La información proporcionada por la asistente sobre el precio de los departamentos se ajusta a los criterios mínimos (3.3 millones y enganche mínimo de 660 mil) para considerarse correcta?": "No",
    "Información proporcionada por la asistente": "El costo de los departamentos es de 3.1 millones de pesos.",
    "¿Durante la conversación, el cliente o la asistente discutieron si el departamento era para habitar o para inversión?": "Sí",
    "Información relevante sobre la preferencia del cliente en cuanto a habitar o invertir": "La asistente mencionó que los departamentos están diseñados para hacer inversiones y son rentables para Airbnb o rentas de larga estadía.",
    "¿La asistente mencionó la ubicación de los departamentos?": "No",
    "Detalles específicos sobre la ubicación de los departamentos proporcionados por la asistente": "N/A",
    "¿La información sobre la ubicación es precisa según los datos proporcionados?": "N/A",
    "¿La asistente mencionó los esquemas de rendimiento o las rentas de la construcción?": "No",
    "Detalles específicos sobre los esquemas de rendimiento o las rentas de construcción proporcionados por la asistente": "N/A",
    "¿La información proporcionada sobre los esquemas de rendimiento o las rentas de construcción es precisa según los criterios mínimos?": "N/A",
    "¿La asistente extendió una invitación al cliente para una cita?": "Sí",
    "Detalles sobre la invitación a la cita proporcionados por la asistente": "La asistente invitó al cliente a una cita y acordaron encontrarse a las 2 PM.",
    "¿La invitación a la cita fue aceptada?": "Sí",
    "Detalles sobre la fecha y hora de la cita": "La cita fue programada para las 2 PMMMMM."
}

spreadsheet_id = '1EyFOt8CQmxNi9lKRLWCnHIYUCf-mDjLFX6jrFjTPUO0' 

def write_data_to_sheet(informacion_asistente):
    range_name = 'Sheet1!A2:R1'
    values = [list(informacion_asistente.keys()), list(informacion_asistente.values())]
    value_input_option = 'USER_ENTERED'
    body = {
        'values': values
    }
    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))
    print(spreadsheet_id)

write_data_to_sheet(informacion_asistente)

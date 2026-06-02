{{- define "fastapi.name" -}}
fastapi
{{- end -}}

{{- define "fastapi.fullname" -}}
{{ .Release.Name }}-fastapi
{{- end -}}

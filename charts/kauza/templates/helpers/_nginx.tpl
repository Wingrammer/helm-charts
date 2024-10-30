{{/*
Return a secret name with TLS certificates
*/}}
{{- define "kauza.nginx.tls.secret.name" -}}
{{- if .Values.nginx.tls.generateSelfSignedCert }}
{{- include "rasa-common.names.fullname" . }}-nginx-tls
{{- else if .Values.nginx.tls.certificateSecret }}
{{- .Values.nginx.tls.certificateSecret }}
{{- end }}
{{- end -}}

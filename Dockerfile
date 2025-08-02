# هذا السطر هو بداية ملف Dockerfile الخاص بك
FROM astrocrpublic.azurecr.io/runtime:3.0-6

# تغيير المستخدم إلى root لتنفيذ الأوامر التي تحتاج صلاحيات عالية
USER root

# تثبيت git
RUN apt-get update && apt-get install -y git

# نسخ مشروع dbt إلى حاوية Airflow
COPY dbt /opt/airflow/dbt

# منح صلاحيات الكتابة لمجلد dbt
RUN chmod -R a+w /opt/airflow/dbt

# العودة إلى المستخدم الافتراضي
USER astro
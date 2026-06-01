# Diagrama ER en Mermaid

> Generado a partir del esquema actual de `db5019188166_hosting-data_io.sql`.
> Incluye el núcleo relacional y las relaciones explícitas por `FOREIGN KEY`.
> Algunas tablas auxiliares del dump (tickets, backups y vistas) se dejaron fuera o sin relación cuando el SQL no declara FK.

```mermaid
erDiagram
    SUCURSAL {
        int id_sucursal PK
        varchar codigo
        varchar nombre
        varchar direccion
        enum status_operativo
    }

    ROLES {
        int id_rol PK
        varchar nombre_rol
        text descripcion_rol
        enum estatus_rol
    }

    TURNOS {
        int id_turno PK
        varchar nombre_turno
        time hora_entrada
        time hora_salida
        enum estatus_turno
    }

    EMPLEADO {
        int id_empleado PK
        varchar nombre
        varchar apellido
        varchar usuario
        varchar correo_electronico
        int id_rol FK
        int id_sucursal FK
        int id_turno FK
        enum status_empleado
    }

    USUARIO {
        int id_usuario PK
        varchar nombre_completo
        varchar usuario_login
        varchar correo_electronico
        int id_rol FK
        int id_sucursal FK
        int id_turno FK
        enum estado
    }

    usuario_rol {
        int id_usuario PK FK
        int id_rol PK FK
    }

    modulos {
        int id_modulo PK
        varchar nombre_modulo
        varchar archivo_php
    }

    PERMISOS {
        int id_rol PK FK
        int id_modulo PK FK
    }

    users {
        int id PK
        varchar usuario
        varchar correo
        varchar estatus
        int id_ruta_usuario
    }

    user_settings {
        int id_config PK
        int user_id FK
        varchar conexion_status
        int intervalo_actualizacion
        boolean notificaciones_push
    }

    CLIENTES {
        int id_cliente PK
        varchar nombre_completo
        varchar telefono
        varchar email
        enum tipo_identificacion
        enum estado
    }

    DESCUENTOS {
        int id_descuentos PK
        varchar concepto_descu
        decimal costo_descu
    }

    TIPO_PAGO {
        int id_pago PK
        varchar concepto_pago
        text descripcion
        enum estatus
    }

    TIPO_HABITACION {
        int id_tipo_habitacion PK
        int id_sucursal FK
        varchar nombre_tipo
        int capacidad_estandar
        int capacidad_maxima
        decimal precio_base_estancia_corta
        decimal precio_tiempo_completo
        decimal precio_hora_extra
        enum estatus
    }

    STATUS_HABITACION {
        int id_status_habitacion PK
        varchar nombre_status
        varchar color_indicador
        boolean activo
    }

    HABITACION {
        int id_habitacion PK
        varchar numero_habitacion
        int id_tipo_habitacion FK
        int status_habitacion FK
        int id_sucursal FK
        decimal precio_4_horas
        decimal precio_tiempo_completo
        int capacidad
        boolean deleted
    }

    BITACORA_HABITACION {
        int id_bitacora_habita PK
        int id_status_habitacion FK
        int id_habitacion FK
        date fecha_bitacora
        time hora_bitacora
        varchar observaciones
    }

    VALIDACION_STATUS_HABITACION {
        int id_validacion PK
        int id_bitacora_habita
        int id_usuario
        datetime fecha_validacion
        varchar estatus_validado
    }

    HISTORIAL_STATUS_HABITACION {
        int id_historial PK
        int id_habitacion
        int id_sucursal
        varchar status_anterior
        varchar status_nuevo
        datetime fecha_cambio
        int id_usuario
    }

    PERSONAS_EXTRA {
        int id_personas_extra PK
        int id_tipo_habitacion FK
        int id_sucursal FK
        int numero_personas
        decimal costo_personas
        boolean activo
    }

    REGISTRO_CLIENTE {
        int id_registro PK
        int id_cliente FK
        int id_empleado FK
        int id_empleado_checkout FK
        int id_habitacion FK
        int id_sucursal FK
        int id_descuento FK
        int id_personas_extra FK
        int id_pago FK
        date fecha_checkin
        date fecha_checkout_estimada
        enum estado_estancia
        varchar tipo_estancia
        decimal monto_total
        boolean pagado
    }

    EXTENSIONES_ESTANCIA {
        int id_extension PK
        int id_registro FK
        int id_tipo_pago FK
        int id_empleado FK
        date fecha_extension
        time tiempo_adicional
        decimal monto_extension
        boolean pagado
    }

    PAGOS {
        int id_pago PK
        int id_registro FK
        int id_tipo_pago FK
        int id_empleado FK
        decimal monto
        date fecha_pago
        time hora_pago
        varchar concepto
    }

    PAGOS_ESTANCIA {
        int id_pago_estancia PK
        int id_estancia FK
        int id_tipo_pago FK
        int id_empleado FK
        enum concepto
        decimal monto
        datetime fecha_pago
    }

    CATEGORIA {
        int id_categoria PK
        varchar nombre
        varchar color
        enum estado
    }

    PRODUCTO {
        int id_producto PK
        varchar sku
        varchar nombre
        int id_sucursal FK
        int id_categoria FK
        decimal costo
        decimal precio_venta
        int stock_actual
        enum estado
    }

    SERVIBAR {
        int id_consumo PK
        int id_estancia FK
        int id_producto FK
        int id_tipo_pago FK
        int id_empleado FK
        int cantidad
        decimal subtotal
        datetime fecha_consumo
        enum estado_pago
    }

    MOVIMIENTOS_INVENTARIO {
        int id_movimiento PK
        int id_producto FK
        int id_servibar FK
        enum tipo_movimiento
        int cantidad
        int stock_anterior
        int stock_nuevo
        datetime fecha_movimiento
    }

    GASTOS {
        int id_gastos PK
        varchar concepto_gastos
        int id_empleado_registro FK
        enum estatus_gastos
        boolean eliminado
    }

    SUBCATEGORIA_GASTOS {
        int id_subcategoria PK
        int id_gastos FK
        varchar nombre_subcategoria
        enum estatus_subcategoria
        boolean eliminado
    }

    ENLACE_GASTOS {
        int id_enlace_gastos PK
        int id_gastos FK
        int id_subcategoria FK
        int id_empleado FK
        int id_tipo_pago FK
        int id_empleado_registro FK
        int id_sucursal FK
        date fecha_gastos
        decimal monto_gasto
        varchar destino_gasto
        boolean eliminado
    }

    FOLIO_TICKETS {
        int id_folio_ticket PK
        int id_sucursal
        varchar codigo_sucursal
        varchar tipo_ticket
        varchar serie
        int ultimo_folio
        boolean activo
    }

    folio_consecutivo_ticket {
        varchar tipo_ticket PK
        int id_sucursal PK
        varchar serie PK
        int ultimo_folio
    }

    TICKETS_CHECKIN {
        int id_ticket PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        datetime fecha_impresion
    }

    TICKETS_CHECKIN_RE_IMPRESION {
        int id_ticket_checkin PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        timestamp fecha_creacion
    }

    TICKETS_PERSONAS_EXTRA_RE_IMPRESION {
        int id_ticket_personas_extra PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total_con_iva
        datetime fecha_ticket
    }

    TICKET_CHECKIN_STORAGE {
        int id_ticket_storage PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        datetime fecha_ticket
    }

    Ticket_Consumo {
        int id_ticket_storage PK
        int id_registro
        int id_sucursal
        varchar folio_ticket
        decimal total
        timestamp fecha_guardado
    }

    Ticket_Consumo_Detalle {
        int id_detalle PK
        int id_ticket_storage FK
        int cantidad
        varchar descripcion
        decimal importe
    }

    TICKET_EXTENSION_STORAGE {
        int id_ticket_storage PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        datetime fecha_registro
    }

    TICKET_TIEMPO_COMPLETO_STORAGE {
        int id_ticket_storage PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        datetime fecha_ticket
    }

    bitacora_acciones {
        int id_log PK
        datetime fecha_hora
        varchar usuario
        varchar modulo
        varchar accion
        int id_registro
        enum resultado
    }

    %% Relaciones explícitas declaradas en el SQL
    SUCURSAL ||--o{ EMPLEADO : "id_sucursal"
    ROLES ||--o{ EMPLEADO : "id_rol"
    TURNOS ||--o{ EMPLEADO : "id_turno"

    SUCURSAL ||--o{ USUARIO : "id_sucursal"
    ROLES ||--o{ USUARIO : "id_rol"
    TURNOS ||--o{ USUARIO : "id_turno"

    USUARIO ||--o{ usuario_rol : "id_usuario"
    ROLES ||--o{ usuario_rol : "id_rol"

    ROLES ||--o{ PERMISOS : "id_rol"
    modulos ||--o{ PERMISOS : "id_modulo"

    users ||--o{ user_settings : "user_id"

    SUCURSAL ||--o{ TIPO_HABITACION : "id_sucursal"
    TIPO_HABITACION ||--o{ HABITACION : "id_tipo_habitacion"
    STATUS_HABITACION ||--o{ HABITACION : "status_habitacion"
    SUCURSAL ||--o{ HABITACION : "id_sucursal"

    STATUS_HABITACION ||--o{ BITACORA_HABITACION : "id_status_habitacion"
    HABITACION ||--o{ BITACORA_HABITACION : "id_habitacion"

    TIPO_HABITACION ||--o{ PERSONAS_EXTRA : "id_tipo_habitacion"
    SUCURSAL ||--o{ PERSONAS_EXTRA : "id_sucursal"

    CLIENTES ||--o{ REGISTRO_CLIENTE : "id_cliente"
    EMPLEADO ||--o{ REGISTRO_CLIENTE : "id_empleado"
    EMPLEADO ||--o{ REGISTRO_CLIENTE : "id_empleado_checkout"
    HABITACION ||--o{ REGISTRO_CLIENTE : "id_habitacion"
    SUCURSAL ||--o{ REGISTRO_CLIENTE : "id_sucursal"
    DESCUENTOS ||--o{ REGISTRO_CLIENTE : "id_descuento"
    PERSONAS_EXTRA ||--o{ REGISTRO_CLIENTE : "id_personas_extra"
    TIPO_PAGO ||--o{ REGISTRO_CLIENTE : "id_pago"

    REGISTRO_CLIENTE ||--o{ EXTENSIONES_ESTANCIA : "id_registro"
    EMPLEADO ||--o{ EXTENSIONES_ESTANCIA : "id_empleado"
    TIPO_PAGO ||--o{ EXTENSIONES_ESTANCIA : "id_tipo_pago"

    REGISTRO_CLIENTE ||--o{ PAGOS : "id_registro"
    TIPO_PAGO ||--o{ PAGOS : "id_tipo_pago"
    EMPLEADO ||--o{ PAGOS : "id_empleado"

    REGISTRO_CLIENTE ||--o{ PAGOS_ESTANCIA : "id_estancia"
    TIPO_PAGO ||--o{ PAGOS_ESTANCIA : "id_tipo_pago"
    EMPLEADO ||--o{ PAGOS_ESTANCIA : "id_empleado"

    SUCURSAL ||--o{ PRODUCTO : "id_sucursal"
    CATEGORIA ||--o{ PRODUCTO : "id_categoria"

    REGISTRO_CLIENTE ||--o{ SERVIBAR : "id_estancia"
    PRODUCTO ||--o{ SERVIBAR : "id_producto"
    TIPO_PAGO ||--o{ SERVIBAR : "id_tipo_pago"
    EMPLEADO ||--o{ SERVIBAR : "id_empleado"

    PRODUCTO ||--o{ MOVIMIENTOS_INVENTARIO : "id_producto"
    SERVIBAR ||--o{ MOVIMIENTOS_INVENTARIO : "id_servibar"

    EMPLEADO ||--o{ GASTOS : "id_empleado_registro"
    GASTOS ||--o{ SUBCATEGORIA_GASTOS : "id_gastos"

    GASTOS ||--o{ ENLACE_GASTOS : "id_gastos"
    SUBCATEGORIA_GASTOS ||--o{ ENLACE_GASTOS : "id_subcategoria"
    EMPLEADO ||--o{ ENLACE_GASTOS : "id_empleado"
    EMPLEADO ||--o{ ENLACE_GASTOS : "id_empleado_registro"
    TIPO_PAGO ||--o{ ENLACE_GASTOS : "id_tipo_pago"
    SUCURSAL ||--o{ ENLACE_GASTOS : "id_sucursal"

    Ticket_Consumo ||--o{ Ticket_Consumo_Detalle : "id_ticket_storage"
```
# Diagrama ER en Mermaid

> Generado a partir del esquema actual de `db5019188166_hosting-data_io.sql`.
> Incluye el núcleo relacional y las relaciones explícitas por `FOREIGN KEY`.
> Algunas tablas auxiliares del dump (tickets, backups y vistas) se dejaron fuera o sin relación cuando el SQL no declara FK.

```mermaid
erDiagram
    SUCURSAL {
        int id_sucursal PK
        varchar codigo
        varchar nombre
        varchar direccion
        enum status_operativo
    }

    ROLES {
        int id_rol PK
        varchar nombre_rol
        text descripcion_rol
        enum estatus_rol
    }

    TURNOS {
        int id_turno PK
        varchar nombre_turno
        time hora_entrada
        time hora_salida
        enum estatus_turno
    }

    EMPLEADO {
        int id_empleado PK
        varchar nombre
        varchar apellido
        varchar usuario
        varchar correo_electronico
        int id_rol FK
        int id_sucursal FK
        int id_turno FK
        enum status_empleado
    }

    USUARIO {
        int id_usuario PK
        varchar nombre_completo
        varchar usuario_login
        varchar correo_electronico
        int id_rol FK
        int id_sucursal FK
        int id_turno FK
        enum estado
    }

    usuario_rol {
        int id_usuario PK FK
        int id_rol PK FK
    }

    modulos {
        int id_modulo PK
        varchar nombre_modulo
        varchar archivo_php
    }

    PERMISOS {
        int id_rol PK FK
        int id_modulo PK FK
    }

    users {
        int id PK
        varchar usuario
        varchar correo
        varchar estatus
        int id_ruta_usuario
    }

    user_settings {
        int id_config PK
        int user_id FK
        varchar conexion_status
        int intervalo_actualizacion
        boolean notificaciones_push
    }

    CLIENTES {
        int id_cliente PK
        varchar nombre_completo
        varchar telefono
        varchar email
        enum tipo_identificacion
        enum estado
    }

    DESCUENTOS {
        int id_descuentos PK
        varchar concepto_descu
        decimal costo_descu
    }

    TIPO_PAGO {
        int id_pago PK
        varchar concepto_pago
        text descripcion
        enum estatus
    }

    TIPO_HABITACION {
        int id_tipo_habitacion PK
        int id_sucursal FK
        varchar nombre_tipo
        int capacidad_estandar
        int capacidad_maxima
        decimal precio_base_estancia_corta
        decimal precio_tiempo_completo
        decimal precio_hora_extra
        enum estatus
    }

    STATUS_HABITACION {
        int id_status_habitacion PK
        varchar nombre_status
        varchar color_indicador
        boolean activo
    }

    HABITACION {
        int id_habitacion PK
        varchar numero_habitacion
        int id_tipo_habitacion FK
        int status_habitacion FK
        int id_sucursal FK
        decimal precio_4_horas
        decimal precio_tiempo_completo
        int capacidad
        boolean deleted
    }

    BITACORA_HABITACION {
        int id_bitacora_habita PK
        int id_status_habitacion FK
        int id_habitacion FK
        date fecha_bitacora
        time hora_bitacora
        varchar observaciones
    }

    VALIDACION_STATUS_HABITACION {
        int id_validacion PK
        int id_bitacora_habita
        int id_usuario
        datetime fecha_validacion
        varchar estatus_validado
    }

    HISTORIAL_STATUS_HABITACION {
        int id_historial PK
        int id_habitacion
        int id_sucursal
        varchar status_anterior
        varchar status_nuevo
        datetime fecha_cambio
        int id_usuario
    }

    PERSONAS_EXTRA {
        int id_personas_extra PK
        int id_tipo_habitacion FK
        int id_sucursal FK
        int numero_personas
        decimal costo_personas
        boolean activo
    }

    REGISTRO_CLIENTE {
        int id_registro PK
        int id_cliente FK
        int id_empleado FK
        int id_empleado_checkout FK
        int id_habitacion FK
        int id_sucursal FK
        int id_descuento FK
        int id_personas_extra FK
        int id_pago FK
        date fecha_checkin
        date fecha_checkout_estimada
        enum estado_estancia
        varchar tipo_estancia
        decimal monto_total
        boolean pagado
    }

    EXTENSIONES_ESTANCIA {
        int id_extension PK
        int id_registro FK
        int id_tipo_pago FK
        int id_empleado FK
        date fecha_extension
        time tiempo_adicional
        decimal monto_extension
        boolean pagado
    }

    PAGOS {
        int id_pago PK
        int id_registro FK
        int id_tipo_pago FK
        int id_empleado FK
        decimal monto
        date fecha_pago
        time hora_pago
        varchar concepto
    }

    PAGOS_ESTANCIA {
        int id_pago_estancia PK
        int id_estancia FK
        int id_tipo_pago FK
        int id_empleado FK
        enum concepto
        decimal monto
        datetime fecha_pago
    }

    CATEGORIA {
        int id_categoria PK
        varchar nombre
        varchar color
        enum estado
    }

    PRODUCTO {
        int id_producto PK
        varchar sku
        varchar nombre
        int id_sucursal FK
        int id_categoria FK
        decimal costo
        decimal precio_venta
        int stock_actual
        enum estado
    }

    SERVIBAR {
        int id_consumo PK
        int id_estancia FK
        int id_producto FK
        int id_tipo_pago FK
        int id_empleado FK
        int cantidad
        decimal subtotal
        datetime fecha_consumo
        enum estado_pago
    }

    MOVIMIENTOS_INVENTARIO {
        int id_movimiento PK
        int id_producto FK
        int id_servibar FK
        enum tipo_movimiento
        int cantidad
        int stock_anterior
        int stock_nuevo
        datetime fecha_movimiento
    }

    GASTOS {
        int id_gastos PK
        varchar concepto_gastos
        int id_empleado_registro FK
        enum estatus_gastos
        boolean eliminado
    }

    SUBCATEGORIA_GASTOS {
        int id_subcategoria PK
        int id_gastos FK
        varchar nombre_subcategoria
        enum estatus_subcategoria
        boolean eliminado
    }

    ENLACE_GASTOS {
        int id_enlace_gastos PK
        int id_gastos FK
        int id_subcategoria FK
        int id_empleado FK
        int id_tipo_pago FK
        int id_empleado_registro FK
        int id_sucursal FK
        date fecha_gastos
        decimal monto_gasto
        varchar destino_gasto
        boolean eliminado
    }

    FOLIO_TICKETS {
        int id_folio_ticket PK
        int id_sucursal
        varchar codigo_sucursal
        varchar tipo_ticket
        varchar serie
        int ultimo_folio
        boolean activo
    }

    folio_consecutivo_ticket {
        varchar tipo_ticket PK
        int id_sucursal PK
        varchar serie PK
        int ultimo_folio
    }

    TICKETS_CHECKIN {
        int id_ticket PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        datetime fecha_impresion
    }

    TICKETS_CHECKIN_RE_IMPRESION {
        int id_ticket_checkin PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        timestamp fecha_creacion
    }

    TICKETS_PERSONAS_EXTRA_RE_IMPRESION {
        int id_ticket_personas_extra PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total_con_iva
        datetime fecha_ticket
    }

    TICKET_CHECKIN_STORAGE {
        int id_ticket_storage PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        datetime fecha_ticket
    }

    Ticket_Consumo {
        int id_ticket_storage PK
        int id_registro
        int id_sucursal
        varchar folio_ticket
        decimal total
        timestamp fecha_guardado
    }

    Ticket_Consumo_Detalle {
        int id_detalle PK
        int id_ticket_storage FK
        int cantidad
        varchar descripcion
        decimal importe
    }

    TICKET_EXTENSION_STORAGE {
        int id_ticket_storage PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        datetime fecha_registro
    }

    TICKET_TIEMPO_COMPLETO_STORAGE {
        int id_ticket_storage PK
        int id_estancia
        int id_sucursal
        varchar folio
        decimal total
        datetime fecha_ticket
    }

    bitacora_acciones {
        int id_log PK
        datetime fecha_hora
        varchar usuario
        varchar modulo
        varchar accion
        int id_registro
        enum resultado
    }

    %% Relaciones explícitas declaradas en el SQL
    SUCURSAL ||--o{ EMPLEADO : "id_sucursal"
    ROLES ||--o{ EMPLEADO : "id_rol"
    TURNOS ||--o{ EMPLEADO : "id_turno"

    SUCURSAL ||--o{ USUARIO : "id_sucursal"
    ROLES ||--o{ USUARIO : "id_rol"
    TURNOS ||--o{ USUARIO : "id_turno"

    USUARIO ||--o{ usuario_rol : "id_usuario"
    ROLES ||--o{ usuario_rol : "id_rol"

    ROLES ||--o{ PERMISOS : "id_rol"
    modulos ||--o{ PERMISOS : "id_modulo"

    users ||--o{ user_settings : "user_id"

    SUCURSAL ||--o{ TIPO_HABITACION : "id_sucursal"
    TIPO_HABITACION ||--o{ HABITACION : "id_tipo_habitacion"
    STATUS_HABITACION ||--o{ HABITACION : "status_habitacion"
    SUCURSAL ||--o{ HABITACION : "id_sucursal"

    STATUS_HABITACION ||--o{ BITACORA_HABITACION : "id_status_habitacion"
    HABITACION ||--o{ BITACORA_HABITACION : "id_habitacion"

    TIPO_HABITACION ||--o{ PERSONAS_EXTRA : "id_tipo_habitacion"
    SUCURSAL ||--o{ PERSONAS_EXTRA : "id_sucursal"

    CLIENTES ||--o{ REGISTRO_CLIENTE : "id_cliente"
    EMPLEADO ||--o{ REGISTRO_CLIENTE : "id_empleado"
    EMPLEADO ||--o{ REGISTRO_CLIENTE : "id_empleado_checkout"
    HABITACION ||--o{ REGISTRO_CLIENTE : "id_habitacion"
    SUCURSAL ||--o{ REGISTRO_CLIENTE : "id_sucursal"
    DESCUENTOS ||--o{ REGISTRO_CLIENTE : "id_descuento"
    PERSONAS_EXTRA ||--o{ REGISTRO_CLIENTE : "id_personas_extra"
    TIPO_PAGO ||--o{ REGISTRO_CLIENTE : "id_pago"

    REGISTRO_CLIENTE ||--o{ EXTENSIONES_ESTANCIA : "id_registro"
    EMPLEADO ||--o{ EXTENSIONES_ESTANCIA : "id_empleado"
    TIPO_PAGO ||--o{ EXTENSIONES_ESTANCIA : "id_tipo_pago"

    REGISTRO_CLIENTE ||--o{ PAGOS : "id_registro"
    TIPO_PAGO ||--o{ PAGOS : "id_tipo_pago"
    EMPLEADO ||--o{ PAGOS : "id_empleado"

    REGISTRO_CLIENTE ||--o{ PAGOS_ESTANCIA : "id_estancia"
    TIPO_PAGO ||--o{ PAGOS_ESTANCIA : "id_tipo_pago"
    EMPLEADO ||--o{ PAGOS_ESTANCIA : "id_empleado"

    SUCURSAL ||--o{ PRODUCTO : "id_sucursal"
    CATEGORIA ||--o{ PRODUCTO : "id_categoria"

    REGISTRO_CLIENTE ||--o{ SERVIBAR : "id_estancia"
    PRODUCTO ||--o{ SERVIBAR : "id_producto"
    TIPO_PAGO ||--o{ SERVIBAR : "id_tipo_pago"
    EMPLEADO ||--o{ SERVIBAR : "id_empleado"

    PRODUCTO ||--o{ MOVIMIENTOS_INVENTARIO : "id_producto"
    SERVIBAR ||--o{ MOVIMIENTOS_INVENTARIO : "id_servibar"

    EMPLEADO ||--o{ GASTOS : "id_empleado_registro"
    GASTOS ||--o{ SUBCATEGORIA_GASTOS : "id_gastos"

    GASTOS ||--o{ ENLACE_GASTOS : "id_gastos"
    SUBCATEGORIA_GASTOS ||--o{ ENLACE_GASTOS : "id_subcategoria"
    EMPLEADO ||--o{ ENLACE_GASTOS : "id_empleado"
    EMPLEADO ||--o{ ENLACE_GASTOS : "id_empleado_registro"
    TIPO_PAGO ||--o{ ENLACE_GASTOS : "id_tipo_pago"
    SUCURSAL ||--o{ ENLACE_GASTOS : "id_sucursal"

    Ticket_Consumo ||--o{ Ticket_Consumo_Detalle : "id_ticket_storage"
```


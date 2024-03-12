from typing import Any, ClassVar

from django.contrib.gis.db.backends.base.models import SpatialRefSysMixin
from django.db import models
from typing_extensions import Self

from django_stubs_ext.db.models import ModelMeta as _ModelMeta

class PostGISGeometryColumns(models.Model):
    f_table_catalog: Any
    f_table_schema: Any
    f_table_name: Any
    f_geometry_column: Any
    coord_dimension: Any
    srid: Any
    type: Any
    objects: ClassVar[models.Manager[Self]]
    Meta: ClassVar[type[_ModelMeta]]

    @classmethod
    def table_name_col(cls) -> Any: ...
    @classmethod
    def geom_col_name(cls) -> Any: ...

class PostGISSpatialRefSys(models.Model, SpatialRefSysMixin):
    srid: Any
    auth_name: Any
    auth_srid: Any
    srtext: Any
    proj4text: Any
    objects: ClassVar[models.Manager[Self]]
    Meta: ClassVar[type[_ModelMeta]]

    @property
    def wkt(self) -> Any: ...

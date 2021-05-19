from typing import Tuple, Type

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SourceStageSpecifier


class LayerSegmentsSourceStageSpecifier(SourceStageSpecifier):
    """
    Specifies the source components for reading the layer-segments format.
    """
    @classmethod
    def description(cls) -> str:
        return "Reads in the layer-segments image-segmentation format from disk, " \
               "where each label has a binary PNG storing the mask for that label"

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.segmentation import ImageSegmentationDomainSpecifier
        return ImageSegmentationDomainSpecifier

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from wai.annotations.core.component.util import LocalFilenameSource
        from ..component import FromLayerSegments
        return LocalFilenameSource, FromLayerSegments
